from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

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
    query = input("Enter your query (or type 'exit' to quit): ")
    
    # Check if the user wants to exit the loop
    if query.lower() == 'exit':
        break

    # Stream the response for the current query
    for chunks in chain.stream({"input": query}):
        print(chunks, end='')

    # Optionally, add a newline or some separation after each response
    print("\n--- End of response ---\n")
