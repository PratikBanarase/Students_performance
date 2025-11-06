import streamlit as st
import pandas as pd
import pickle

# Load your trained model
model = pickle.load(open('student_performance_model.pkl', 'rb'))

st.set_page_config(page_title="Student Performance Predictor", layout="centered")

# App title and description
st.title("🎓 Student Performance Prediction App")
st.markdown("""
This app predicts a student's **average exam score** based on demographic and educational background data.
Select the input details below and click **Predict Score**.
""")

# Sidebar for inputs
st.sidebar.header("Enter Student Information")

gender = st.sidebar.selectbox("Gender", ["female", "male"])
race = st.sidebar.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parent_edu = st.sidebar.selectbox("Parental Level of Education", [
    "some high school", "high school", "some college", 
    "associate's degree", "bachelor's degree", "master's degree"])
lunch = st.sidebar.selectbox("Lunch Type", ["standard", "free/reduced"])
prep = st.sidebar.selectbox("Test Preparation Course", ["none", "completed"])

# Encode inputs (same way as model training)
gender_enc = 0 if gender == 'female' else 1
race_enc = ["group A","group B","group C","group D","group E"].index(race)
parent_enc = ["some high school","high school","some college","associate's degree","bachelor's degree","master's degree"].index(parent_edu)
lunch_enc = 0 if lunch == 'free/reduced' else 1
prep_enc = 0 if prep == 'none' else 1

# Combin
