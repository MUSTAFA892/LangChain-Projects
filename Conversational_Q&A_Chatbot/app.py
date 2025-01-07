import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_community.llms import Ollama
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai

## Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

from dotenv import load_dotenv
load_dotenv()
import os

# Initialize API key (if needed for any other services)
#os.getenv("GEMINI_API_KEY")
#genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


chat = Ollama(model="llama3.2:1b")
#chat = ChatGoogleGenerativeAI(model="gemini-1.5-pro",temperature=0.3)

# Initialize session state for messages if not already present
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are a AI code assistant.")
    ]

# Function to get chat model response
def get_chatmodel_response(question):
    # Append the user's question to the flow messages
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    
    # Combine the list of messages into a single prompt string
    conversation = "\n".join([message.content for message in st.session_state['flowmessages']])
    
    # Get response from Ollama model
    answer = chat(prompt=conversation)
    
    # Append the AI's response to the flow messages
    st.session_state['flowmessages'].append(AIMessage(content=answer))  # 'answer' is now a string
    
    return answer  # directly returning the string response

# Input field for user question
input = st.text_input("Input: ", key="input")

# Button to submit the question
submit = st.button("Ask the question")

# If the button is clicked, get the response from the model
if submit and input:
    response = get_chatmodel_response(input)
    
    # Display the response
    st.subheader("The Response is")
    st.write(response)
