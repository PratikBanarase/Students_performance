import streamlit as st
import pandas as pd

# --- Configuration and Page Setup ---
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon=":bar_chart:",
    layout="wide"
)

# ===============================================
# === Header Bar Section (Main Title) ==========
# ===============================================
st.title("📊 Student Performance Analysis Dashboard")
st.markdown("---") # Separator line for a clean look

# ===============================================
# === Sidebar Section (Name and Links) ==========
# ===============================================

# Define the personal information - REPLACE WITH YOUR DETAILS
NAME = "Pratik Banarase"
LINKEDIN_URL = "https://www.linkedin.com/in/pratikbanarse/"
GITHUB_URL = "https://github.com/PratikBanarase"
GMAIL_ADDRESS = "pratikbanarse8@gmail.com"

# Sidebar Title
st.sidebar.header("Data Scientist")

# Developer Name
st.sidebar.markdown(f"**{Pratik Sudhakar Banarase}**")

# LinkedIn Link
st.sidebar.markdown(f"**LinkedIn:** [Profile]({https://www.linkedin.com/in/pratikbanarse/})")

# GitHub Link
st.sidebar.markdown(f"**GitHub:** [Repository]({https://github.com/PratikBanarase})")

# Gmail Link (Mailto)
st.sidebar.markdown(f"**Gmail:** [{pratikbanarse8@gmail.com}](mailto:{pratikbanarse8@gmail.com})")

st.sidebar.markdown("---")


# ===============================================
# === Main Application Logic (Data Analysis) ====
# ===============================================

# Function to load data with caching for performance
@st.cache_data
def load_data(file_path):
    """Loads the student performance data."""
    df = pd.read_csv(file_path)
    return df

# Load the data file provided by the user
FILE_NAME = 'StudentsPerformance.csv'

try:
    df = load_data(FILE_NAME)
    st.success(f"Data '{FILE_NAME}' loaded successfully! Total records: {len(df)}")

    # --- Data Preview ---
    st.header("1. Raw Data Preview")
    st.dataframe(df.head(10))

    # --- Descriptive Statistics ---
    st.header("2. Descriptive Statistics")
    st.dataframe(df[['math score', 'reading score', 'writing score']].describe().T)

    # --- Simple Visualization ---
    st.header("3. Math Score Distribution by Gender")

    # Use a radio button in the sidebar for filtering/grouping
    chart_type = st.sidebar.radio(
        "Select Chart Type:",
        ('Bar Chart', 'Histogram')
    )

    if chart_type == 'Bar Chart':
        # Group data to count average scores
        avg_scores = df.groupby('gender')[['math score', 'reading score', 'writing score']].mean()
        st.bar_chart(avg_scores)
    else:
        # Show a simple histogram of math scores
        st.line_chart(df['math score'].value_counts().sort_index())

except FileNotFoundError:
    st.error(f"Error: The file **'{FILE_NAME}'** was not found. Please ensure it is in the same folder as your 'app.py' file.")
except Exception as e:
    st.error(f"An unexpected error occurred while loading the data: {e}")

# --- Footer ---
st.markdown("---")
st.markdown("Developed with Streamlit and Python.")
