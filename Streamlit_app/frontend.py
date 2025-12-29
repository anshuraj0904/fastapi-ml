import streamlit as st
import requests
import pandas as pd

APP_URI = "http://127.0.0.1:8000/predict"




st.title("Insurance Premium Category Predictor")
st.markdown("Enter your details below:")


# Input fields
age = st.number_input("Age", min_value=0, max_value=120, value=30)
weight = st.number_input("Weight (in kgs)", min_value=1.0, value=65.0)
height = st.number_input("Height (in mtrs)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Salary(in LPA)", min_value=0.0, value=2.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value= "Mumbai")
occupation = st.selectbox(
    "Occupation", 
    options=["retired", "freelancer", "student", "government_job", "business_owner", "unemployed", "private_job"]
)




if st.button("Predict Premium Category"):
    input_data = {
        "age":age,
        "weight":weight,
        "height":height,
        "income_lpa":income_lpa,
        "smoker":smoker,
        "city":city,
        "occupation":occupation
    }


    try:
        response = requests.post(APP_URI,json=input_data)
        if response.status_code == 200:
            result = response.json()
            data = result['insurance_premium_category']['class_probabilities']

            df = pd.DataFrame(list(data.items()),columns=["Class", "Probability"])
            st.success(f"Predicted Insurance Premium Category: {result['insurance_premium_category']['predicted category']}")
            st.warning(f"Confidence: {result['insurance_premium_category']['confidence']}")
            st.markdown("### Class Probabilities")
            st.table(df)

        else:
            st.error(f"API Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException:
        st.error("Could not connect to the API, make sure it is running on port 8000")          