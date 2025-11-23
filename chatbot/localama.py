from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
try:
    from langchain_ollama import Ollama  # preferred in newer versions
except ImportError:
    from langchain_community.llms import Ollama  # fallback for older versions
from langchain_huggingface import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import streamlit as st
import torch
from dotenv import load_dotenv
load_dotenv()
#Prompt Templete
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant, Please respond to the user questions"),
        ("user","Question:{question}")
    ]
)

#StreamLit framework
st.title("*** LangChain Chatbot Application ***")
input_text=st.text_input("Search your question here...")

#openAI OLLAMA model
llm=Ollama(model='llama2')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

