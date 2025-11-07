import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# PAGE CONFIGURATION
# -------------------------------
st.set_page_config(page_title="Students Performance Dashboard", layout="wide")

# -------------------------------
# SIDEBAR SECTION
# -------------------------------
st.sidebar.title("📊 Students Performance App")
st.sidebar.markdown("**Created by: Pratik Banarase**")
st.sidebar.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/pratikbanarse/)")
st.sidebar.markdown("[💻 GitHub](https://github.com/PratikBanarase)")
st.sidebar.markdown("✉️ pratikbanars8e@gmail.com")

st.sidebar.header("⚙️ Controls")
uploaded_file = st.sidebar.file_uploader("Upload StudentsPerformance.csv", type=["csv"])

# -------------------------------
# LOAD DATA
# -------------------------------
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("StudentsPerformance.csv")

st.title("🎓 Students Performance Analysis Dashboard")

st.markdown("""
This dashboard allows you to explore the **Students Performance dataset** interactively.
You can visualize how various factors (gender, parental education, test preparation, etc.) 
affect student scores across subjects.
""")

# -------------------------------
# DATA PREVIEW
# -------------------------------
st.subheader("📂 Dataset Preview")
st.dataframe(df.head())

# -------------------------------
# BASIC INFO
# -------------------------------
st.subheader("📈 Dataset Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Total Students", df.shape[0])
col2.metric("Total Columns", df.shape[1])
col3.metric("Unique Genders", df['gender'].nunique())

st.write("### Statistical Summary")
st.dataframe(df.describe())

# -------------------------------
# VISUALIZATION SECTION
# -------------------------------
st.subheader("📊 Visualizations")

# Select columns for visualization
x_axis = st.selectbox("Select X-axis", df.columns)
y_axis = st.selectbox("Select Y-axis", df.select_dtypes(include='number').columns)

# Box Plot
st.write("### Box Plot")
fig_box = px.box(df, x=x_axis, y=y_axis, color=x_axis,
                 title=f"Boxplot of {y_axis} by {x_axis}")
st.plotly_chart(fig_box, use_container_width=True)

# Histogram
st.write("### Distribution of Scores")
selected_score = st.selectbox("Select Score Column", 
                              ['math score', 'reading score', 'writing score'])
fig_hist = px.histogram(df, x=selected_score, nbins=20, color='gender',
                        title=f"Distribution of {selected_score}")
st.plotly_chart(fig_hist, use_container_width=True)

# Scatter Plot
st.write("### Correlation Between Scores")
fig_scatter = px.scatter(df, x='math score', y='reading score',
                         color='gender', size='writing score',
                         title='Math vs Reading Scores (bubble size = Writing score)')
st.plotly_chart(fig_scatter, use_container_width=True)

# -------------------------------
# INSIGHTS
# -------------------------------
st.subheader("🧠 Insights")
st.markdown("""
- **Gender differences:** Compare average scores by gender.
- **Parental education impact:** Observe how parental education affects performance.
- **Test preparation:** Students who completed test preparation tend to score higher.
""")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.markdown("📘 **Developed by Pratik Banarase** | Using Streamlit + Plotly + Pandas")

