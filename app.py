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
    race_enc = ["group A","group B","group C","group D","group E"].index(race)
    parent_enc = ["some high school","high school","some college",
                  "associate's degree","bachelor's degree","master's degree"].index(parent_edu)
    lunch_enc = 0 if lunch == 'free/reduced' else 1
    prep_enc = 0 if prep == 'none' else 1

    # Create input DataFrame
    input_data = pd.DataFrame([[gender_enc, race_enc, parent_enc, lunch_enc, prep_enc]],
                              columns=['gender','race/ethnicity','parental level of education','lunch','test preparation course'])

    # Predict score
    predicted_score = model.predict(input_data)[0]

    # Display results
    st.subheader("📘 Predicted Average Exam Score:")
    st.success(f"{predicted_score:.2f}")

    # Determine grade
    if predicted_score >= 90:
        grade = "A+ (Excellent)"
    elif predicted_score >= 80:
        grade = "A (Very Good)"
    elif predicted_score >= 70:
        grade = "B (Good)"
    elif predicted_score >= 60:
        grade = "C (Average)"
    else:
        grade = "D (Needs Improvement)"

    st.subheader("🎯 Predicted Grade:")
    st.info(grade)

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Scikit-Learn")
