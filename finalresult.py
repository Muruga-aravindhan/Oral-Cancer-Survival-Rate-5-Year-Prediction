import streamlit as st
import pickle
import numpy as np

# Load the trained model
model_path = "5_Year_suvival_rate_prediction_model.pkl"  # Make sure the file is in the same directory
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Title
st.title("Oral Cancer Survival Rate (5-Year, %) Prediction")

# User Input Fields
age = st.number_input("Age", min_value=0, max_value=100, value=50)
tobacco_use = st.selectbox("Tobacco Use", ["No", "Yes"])
alcohol_use = st.selectbox("Alcohol Use", ["No", "Yes"])
hpv_infection = st.selectbox("HPV Infection", ["No", "Yes"])
tumor_size = st.number_input("Tumor Size (cm)", min_value=0.1, max_value=10.0, value=2.5)

# Convert categorical inputs to numeric
tobacco_use = 1 if tobacco_use == "Yes" else 0
alcohol_use = 1 if alcohol_use == "Yes" else 0
hpv_infection = 1 if hpv_infection == "Yes" else 0

# Predict button
if st.button("Predict Survival Rate"):
    # Create input array
    input_data = np.array([[age, tobacco_use, alcohol_use, hpv_infection, tumor_size]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display result
    st.success(f"Predicted 5-Year Survival Rate: {prediction:.2f}%")
