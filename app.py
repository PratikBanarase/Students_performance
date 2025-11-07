# app.py
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder

# ------------------- PAGE CONFIG -------------------
st.set_page_config(page_title="Students Performance Predictor", page_icon="🎓", layout="wide")

# ------------------- HEADER SECTION -------------------
st.title("🎓 Student Performance Prediction App")
st.markdown("Predict student exam scores based on study and demographic factors using ML.")

# ------------------- SIDEBAR SECTION -------------------
st.sidebar.header("👤 Data analysts")
st.sidebar.markdown("""
**Name:** Pratik Banarse  
[LinkedIn](https://www.linkedin.com) | [GitHub](https://github.com) | [Gmail](mailto:example@gmail.com)
""")



# ------------------- LOAD DATASET -------------------
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("students_performance.csv")

st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

# ------------------- DATA PREPROCESSING -------------------
df.columns = df.columns.str.strip()

le = LabelEncoder()
for col in ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']:
    df[col] = le.fit_transform(df[col])

# Features and target
X = df[['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course',
        'math score', 'reading score']]
y = df['writing score']

# ------------------- TRAIN MODEL -------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# ------------------- USER INPUT SECTION -------------------
st.header("🧾 Enter Student Details for Prediction")

gender = st.selectbox("Gender", ("female", "male"))
race = st.selectbox("Race/Ethnicity", ("group A", "group B", "group C", "group D", "group E"))
parent_edu = st.selectbox("Parental Level of Education", (
    "some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"))
lunch = st.selectbox("Lunch Type", ("standard", "free/reduced"))
test_prep = st.selectbox("Test Preparation Course", ("none", "completed"))
math_score = st.slider("Math Score", 0, 100, 60)
reading_score = st.slider("Reading Score", 0, 100, 60)

# Encode user input
input_data = pd.DataFrame({
    'gender': [le.fit(df['gender']).transform([gender])[0]],
    'race/ethnicity': [le.fit(df['race/ethnicity']).transform([race])[0]],
    'parental level of education': [le.fit(df['parental level of education']).transform([parent_edu])[0]],
    'lunch': [le.fit(df['lunch']).transform([lunch])[0]],
    'test preparation course': [le.fit(df['test preparation course']).transform([test_prep])[0]],
    'math score': [math_score],
    'reading score': [reading_score]
})

# ------------------- PREDICTION -------------------
if st.button("🎯 Predict Writing Score"):
    prediction = model.predict(input_data)
    st.success(f"✅ Predicted Writing Score: **{prediction[0]:.2f}**")

# ------------------- FOOTER -------------------
st.markdown("---")
st.markdown("**Developed by Pratik Banarse** | © 2025 | [GitHub](https://github.com) | [LinkedIn](https://www.linkedin.com)")
