from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
import speech_recognition as sr
from gtts import gTTS
import os

def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something...")
        audio = r.listen(source)
        print("Got it! Now to recognize it...")
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return "Could not request results from Google Speech Recognition service; {0}".format(e)

# Initialize the LLM once outside the loop
llm = Ollama(model="mistral")

prompt = ChatPromptTemplate.from_messages([
    ("system", "Keep your answers short and to the point. \
     You are talking to elementary school aged children."),
    ("user", "{input}")
])


chain = prompt | llm

while True:
    # Request a new prompt from the user
    #  query = input("Enter your query (or type 'exit' to quit): ")
    query = get_voice_input()

    if query == "Wally":

      print("You said: ", query)

      print("Go ahead and speak")
    
      query = get_voice_input()

      
      # Check if the user wants to exit the loop
      if query.lower() == 'exit':
         break


      # Stream the response for the current query
      # for chunks in chain.stream({"input": query}):
         # print(chunks, end='')
      response = chain({"input": query}) 
      tts = gTTS(text=response, lang='en')
      tts.save("response.mp3")
      os.system("mpg321 response.mp3")

      # Optionally, add a newline or some separation after each response
      print("\n--- End of response ---\n")
