import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('student_performance_model.pkl', 'rb'))

# Streamlit Page Configuration
st.set_page_config(page_title="🎓 Student Performance Predictor", layout="wide")

# App Title
st.title("🎓 Student Performance Prediction App")
st.markdown("""
This app predicts a student's **average exam score** based on demographic and educational background data.  
Fill in the details below and click **Predict Score** to see the result.
""")

# Form layout (centered input form)
with st.form(key='input_form'):
    st.header("🧾 Enter Student Information")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["female", "male"])
        race = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
        parent_edu = st.selectbox("Parental Level of Education", [
            "some high school", "high school", "some college",
            "associate's degree", "bachelor's degree", "master's degree"])

    with col2:
        lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
        prep = st.selectbox("Test Preparation Course", ["none", "completed"])

    # Submit button (centered and clear)
    submit_button = st.form_submit_button(label="🎯 Predict Score")

# When the user clicks the button
if submit_button:
    # Encode categorical inputs (same way as model was trained)
    gender_enc = 0 if gender == 'female' else 1
    race_enc = ["group A","gbr]()_
