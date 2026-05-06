import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Disease Prediction System")

symptoms = ["Fever", "Cough", "Headache", "Fatigue"]

selected = st.multiselect(
    "Select Symptoms",
    symptoms
)

if st.button("Predict"):

    input_data = []

    for symptom in symptoms:
        if symptom in selected:
            input_data.append(1)
        else:
            input_data.append(0)

    prediction = model.predict([input_data])

    st.success(f"Predicted Disease: {prediction[0]}")