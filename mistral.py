from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
import speech_recognition as sr
from gtts import gTTS
import os


def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Unknown value error"
    except sr.RequestError as e:
        return "Could not request results from Google Speech Recognition service; {0}".format(
            e
        )


def play_text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")


# Initialize the LLM once outside the loop
llm = Ollama(model="mistral")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Keep your answers short and to the point. \
     You are talking to an elementary school aged child.",
        ),
        ("user", "{input}"),
    ]
)


chain = prompt | llm

while True:
    # Request a new prompt from the user
    query = get_voice_input()

    if query == "Wally":
        play_text_to_speech("... Hello, I am Wally. How can I help you?")

        query = get_voice_input()
        while query == "Unknown value error":
            query = get_voice_input()
        play_text_to_speech("... You said: " + query)
        play_text_to_speech("... Please wait while I think.")

        # Check if the user wants to exit the loop
        if query.lower() == "exit":
            break

        # send llm respons to text to speech
        # response = chain.invoke({"input": query})
        # play_text_to_speech("... "+response)
        statement = []
        for chunk in chain.stream({"input": query}):
            statement.append(chunk)

            if (
                chunk == "!"
                or chunk == "?"
                or chunk == "."
                or chunk == '."'
                or chunk == '!"'
            ):
                print("".join(statement))
                play_text_to_speech("".join(statement))
                statement = []
         
         # catch any remaining statement
        if len(statement) > 0:
           print("".join(statement))
           play_text_to_speech("".join(statement))
           statement = []

        # Optionally, add a newline or some separation after each response
        print("\n--- End of response ---\n")
