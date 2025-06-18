import streamlit as st
import numpy as np
import pickle

# Load model
model_path = "Diabetesmodel.pkl"
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()

# App title
st.title(" Diabetes Risk Assessment")

# User Inputs
glucose = st.number_input("Glucose Level", min_value=0.0, format="%.2f")
bp = st.number_input("Blood Pressure", min_value=0.0, format="%.2f")
bmi = st.number_input("BMI", min_value=0.0, format="%.2f")
age = st.number_input("Age", min_value=0, step=1)

# Prediction button
if st.button("Predict"):
    input_data = np.array([[glucose, bp, bmi, age]])
    prediction = model.predict(input_data)
    result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
    st.success(f"The person is likely: **{result}**")
