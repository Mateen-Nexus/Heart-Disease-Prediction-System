
import streamlit as st
import numpy as np
import pickle

st.title("❤️ Heart Disease Prediction App")


age = st.number_input("Age", min_value=1, max_value=120, value=45)
sex = st.selectbox("Sex", ["Male", "Female"])
bp = st.number_input("Blood Pressure", min_value=50, max_value=250, value=120)
chol = st.number_input("Cholesterol", min_value=100, max_value=600, value=200)

if st.button("Predict"):

    sex_val = 1 if sex == "Male" else 0


    if age > 50 or bp > 130 or chol > 240:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")
