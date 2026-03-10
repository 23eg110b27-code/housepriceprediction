import streamlit as st
import numpy as np

st.title("House Price Prediction")

area = st.number_input("Enter area")
age = st.number_input("Enter house age")

if st.button("Predict"):
    price = area * 1000 - age * 500
    st.success(f"Predicted price: {price}")