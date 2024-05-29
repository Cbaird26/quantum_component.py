import streamlit as st
import numpy as np
from ai_component import make_prediction
from quantum_component import run_quantum_circuit

st.title("AI and Quantum Computing Chatbot")

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Function to display chat history
def display_chat_history():
    for i, chat in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(f"**User:** {chat}")
        else:
            st.write(f"**Bot:** {chat}")

# Function to process user input and generate a response
def process_input(user_input):
    if "quantum" in user_input.lower():
        quantum_result = run_quantum_circuit()
        response = f"Quantum Circuit Result: {quantum_result}"
    elif "predict" in user_input.lower():
        input_data = np.array([float(x) for x in user_input.split(",")]).reshape(1, -1)
        prediction = make_prediction(input_data)
        response = f"AI Prediction: {np.argmax(prediction, axis=1)}"
    else:
        response = "I'm sorry, I didn't understand that. Please ask about quantum circuits or AI predictions."
    
    return response

# User input
user_input = st.text_input("You:", key="user_input")

# Process and display chat when the user presses Enter
if st.button("Send"):
    st.session_state.chat_history.append(user_input)
    bot_response = process_input(user_input)
    st.session_state.chat_history.append(bot_response)
    st.session_state.user_input = ""  # Clear input field

# Display chat history
display_chat_history()
