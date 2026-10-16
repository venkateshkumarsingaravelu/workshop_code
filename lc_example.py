from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()

llm = ChatOpenAI(
    model="qwen/qwen-2.5-7b-instruct",   # any OpenRouter model
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

response = llm.invoke("Explain LangChain in one sentence.")
print(response.content)

# Example 2

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(

    
    "Explain {topic} in simple terms."
)

chain = prompt | llm

print(chain.invoke({"topic": "Food"}).content)
print(chain.invoke({"topic": "Travel"}).content)



from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(
    model="qwen/qwen-2.5-7b-instruct",
    api_key="YOUR_OPENROUTER_API_KEY",
    base_url="https://openrouter.ai/api/v1"
)

memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=memory
)

print(conversation.run("My name is Venkatesh."))
print(conversation.run("What is my name?"))
