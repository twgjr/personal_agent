import sys
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from models import ModelNotFoundException, check_model_pulled



def main():
   if len(sys.argv) > 1:
        if(len(sys.argv) > 2):
            return

        try:
           check_model_pulled(sys.argv[1])
        except ModelNotFoundException as e:
           print(e)
           return
        
        run(sys.argv[1])
   else:
        print("No arguments were passed to the script. \
            Must be a supported model name from Ollama. \
            For example, 'gemma'")


def run(model):
   # Initialize the LLM once outside the loop
   llm = Ollama(model=model)

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
      query = input("User: ")

      # Check if the user wants to exit the loop
      if query.lower() == "exit":
         break

      print("Model: ",end="")
      # send llm response to text to speech
      for chunk in chain.stream({"input": query}):
         print(chunk, end="")
         sys.stdout.flush()

      print()

if(__name__ == "__main__"):
   main()