from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
#from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import os
import uvicorn
try:
    from langchain_ollama import Ollama,OllamaLLM,ChatOllama  # preferred in newer versions
except ImportError:
    from langchain_community.llms import Ollama  # fallback for older versions
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="LangChain Chatbot API",
    description="An API for LangChain Chatbot Application using FastAPI and LangServe",
    version="1.0"
)

# add_routes(
#     app,
#     ChatOpenAI(),
#     path="/openai"
#            )

# model=ChatOpenAI()

#Ollama model
llm=Ollama(model='llama2')

#Prompt Template
#prompt1=ChatPromptTemplate.from_messages("Write me an essay about {topic} with 100 words.")
prompt2=ChatPromptTemplate.from_messages([
    ("system","You are a helpful poet. Keep outputs around 100 words."),
    ("user","TWrite me a poem about {topic}.")
    ])

# add_routes(
#     app,
#     prompt1|model,
#     path="/essay"
# )

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)