import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import plotly.express as px

# ------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------
st.set_page_config(page_title="Students Performance Prediction", layout="wide")

st.title("🎓 Students Performance Prediction App")
st.markdown("Predict student performance using **Linear Regression** and **Gradient Boosting** models.")

# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------
uploaded_file = st.sidebar.file_uploader("📂 Upload StudentsPerformance.csv", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("StudentsPerformance.csv")

st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

# ------------------------------------------------------------
# DATA PREPROCESSING
# ------------------------------------------------------------
df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

# Encode categorical columns
le = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col])

# Features and Target
X = df.drop(columns=['average_score'])
y = df['average_score']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ------------------------------------------------------------
# MODEL TRAINING
# ------------------------------------------------------------
# Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)

# Gradient Boosting
gb_model = GradientBoostingRegressor(random_state=42)
gb_model.fit(X_train, y_train)
gb_pred = gb_model.predict(X_test)

# ------------------------------------------------------------
# MODEL PERFORMANCE
# ------------------------------------------------------------
def model_metrics(y_true, y_pred):
    return {
        "R² Score": round(r2_score(y_true, y_pred), 3),
        "MAE": round(mean_absolute_error(y_true, y_pred), 3),
        "RMSE": round(np.sqrt(mean_squared_error(y_true, y_pred)), 3)
    }

lr_metrics = model_metrics(y_test, lr_pred)
gb_metrics = model_metrics(y_test, gb_pred)

st.subheader("📈 Model Performance Comparison")
col1, col2 = st.columns(2)
with col1:
    st.write("### Linear Regression")
    st.json(lr_metrics)
with col2:
    st.write("### Gradient Boosting")
    st.json(gb_metrics)

# ------------------------------------------------------------
# SIDEBAR INPUTS FOR PREDICTION
# ------------------------------------------------------------
st.sidebar.header("🎯 Predict Student Average Score")

# Generate input widgets dynamically
input_data = {}
for col in X.columns:
    if df[col].dtype == 'int64' or df[col].dtype == 'float64':
        min_val, max_val = int(df[col].min()), int(df[col].max())
        input_data[col] = st.sidebar.slider(col, min_val, max_val, int(df[col].mean()))
    else:
        input_data[col] = st.sidebar.selectbox(col, df[col].unique())

# Convert input to dataframe
input_df = pd.DataFrame([input_data])

# ------------------------------------------------------------
# MAKE PREDICTIONS
# ------------------------------------------------------------
model_choice = st.sidebar.radio("Select Model", ("Linear Regression", "Gradient Boosting"))

if st.sidebar.button("Predict Score"):
    if model_choice == "Linear Regression":
        prediction = lr_model.predict(input_df)[0]
    else:
        prediction = gb_model.predict(input_df)[0]

    st.success(f"🎯 Predicted Average Score ({model_choice}): **{prediction:.2f}**")

# ------------------------------------------------------------
# VISUALIZATION
# ------------------------------------------------------------
st.subheader("📉 Feature Correlation Heatmap")
corr = df.corr()
fig = px.imshow(corr, text_auto=True, aspect="auto", title="Correlation Heatmap")
st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.markdown("---")
st.markdown("👨‍💻 **Developed by Pratik Banarase** | Streamlit + Plotly + Scikit-Learn")
