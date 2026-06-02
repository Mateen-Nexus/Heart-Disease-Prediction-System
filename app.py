import streamlit as st
import numpy as np
import pickle

st.title("❤️ Heart Disease Prediction App")

# simple input form
age = st.number_input("Age")
sex = st.selectbox("Sex", ["Male", "Female"])
bp = st.number_input("Blood Pressure")
chol = st.number_input("Cholesterol")

if st.button("Predict"):

    sex = 1 if sex == "Male" else 0

    # dummy logic (abhi model nahi hai)
    if age > 50 and bp > 130:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")