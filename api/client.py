import requests
import streamlit as st


def get_ollama_response(input_text):
    response=requests.post("http://localhost:8000/poem/invoke",
                           
                         json={'input':{'topic':input_text}})
    return response.json()["output"]

#StreamLit framework
st.title("*** LangChain Chatbot Application using Ollama LLM ***")
input_text=st.text_input("Search your poem topic here...")
if input_text:
    st.write(get_ollama_response(input_text))