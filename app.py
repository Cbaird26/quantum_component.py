# app.py
import streamlit as st
import numpy as np
from ai_component import make_prediction
from quantum_component import run_quantum_circuit

st.title("AI and Quantum Computing Integration")

st.write("This app leverages the power of a quantum computer and AI.")

input_data = st.text_input("Enter input data (comma-separated values):", "5.1,3.5,1.4,0.2")
input_data = np.array([float(x) for x in input_data.split(",")]).reshape(1, -1)

if st.button("Run Quantum Circuit"):
    quantum_result = run_quantum_circuit()
    st.write(f"Quantum Circuit Result: {quantum_result}")

if st.button("Make AI Prediction"):
    prediction = make_prediction(input_data)
    st.write(f"AI Prediction: {np.argmax(prediction, axis=1)}")
