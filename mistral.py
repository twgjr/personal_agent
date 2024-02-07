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
    play_text_to_speech("Ready!")

    try:
        query = get_voice_input()
    except:
        play_text_to_speech("I'm sorry, I didn't catch that. Please try again.")
        continue

    try:
        play_text_to_speech("... You said: " + query + ". Please wait while I think.")
    except:
        continue

    # Check if the user wants to exit the loop
    if query.lower() == "exit":
        break

    # send llm response to text to speech
    statement = []
    for chunk in chain.stream({"input": query}):
        statement.append(chunk)

        # type hint chunk as string
        chunk: str = chunk
        # check if chunk string contains punctuation
        if "!" in chunk or "?" in chunk or "." in chunk:
            print("".join(statement))
            try:
                play_text_to_speech("".join(statement))
                statement = []
            except:
                play_text_to_speech("Something went wrong. Please try again.")
                continue

    # catch any remaining statement
    if len(statement) > 1:
        print("".join(statement))
        try:
            play_text_to_speech("".join(statement))
            statement = []
        except:
            play_text_to_speech("Something went wrong. Please try again.")
            continue

    # Optionally, add a newline or some separation after each response
    print("\n--- End of response ---\n")
