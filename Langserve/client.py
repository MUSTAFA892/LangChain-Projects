import requests
import streamlit as st
 
def get_ollama_response(input_text):
    try:
        # Send a POST request to the API
        response = requests.post(
            "http://localhost:8000/poem/invoke",
            json={'input': {'topic': input_text}}
        )
        
        # Check if the response status code is successful (2xx)
        if response.status_code == 200:
            # Try to parse the response as JSON
            try:
                return response.json().get('output', 'No output key found in response')
            except ValueError as e:
                return f"Error decoding JSON: {e}"
        else:
            return f"Error: Server returned status code {response.status_code}"
    
    except requests.exceptions.RequestException as e:
        return f"Error during request: {e}"

# Streamlit framework
st.title('Shayari generator')
input_text1 = st.text_input("Write a shayari on")

if input_text1:
    st.write(get_ollama_response(input_text1))
