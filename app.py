import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuration and Page Setup ---
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon=":bar_chart:",
    layout="wide"
)

# ===============================================
# === Sidebar Section (Name and Links) ==========
# ===============================================

# --- REPLACE THESE PLACEHOLDERS WITH YOUR ACTUAL DETAILS ---
NAME = "Pratik Banarase"
LINKEDIN_URL = "https://www.linkedin.com/in/pratikbanarse/"
GITHUB_URL = "https://github.com/PratikBanarase"
GMAIL_ADDRESS = "pratikbanarse8@gmail.com"
# -----------------------------------------------------------

with st.sidebar:
    st.header("👤 Data scientist")
    st.markdown(f"{PratikBanarase}")
    
    # LinkedIn Link
    st.markdown(f"**LinkedIn:** [Connect Here]({https://www.linkedin.com/in/pratikbanarse/})")
    
    # GitHub Link
    st.markdown(f"**GitHub:** [View Code]({https://github.com/PratikBanarase})")
    
    # Gmail Link (Mailto format for clicking)
    st.markdown(f"**Email:** [{pratikbanarse8@gmail.com}](mailto:{pratikbanarse8@gmail.com})")
    
    st.markdown("---")
    st.info("💡 Use the filters below to explore the data!")

# ===============================================
# === Header Bar Section (Main Title) ==========
# ===============================================
st.title("📚 Student Performance Analysis Dashboard")
st.markdown("A simple interactive dashboard analyzing student demographic and academic performance.")
st.markdown("---") # Separator line for a clean look

# ===============================================
# === Main Application Logic (Data Analysis) ====
# ===============================================

FILE_NAME = 'StudentsPerformance.csv'

# Function to load data with caching for better performance
@st.cache_data
def load_data(file_path):
    """Loads the student performance data."""
    try:
        df = pd.read_csv(file_path)
        # Clean column names by replacing spaces and '/'
        df.columns = df.columns.str.replace(r'[ /]', '_', regex=True).str.lower()
        return df
    except FileNotFoundError:
        st.error(f"Error: The file **'{file_path}'** was not found.")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred while loading the data: {e}")
        return None

df = load_data(FILE_NAME)

if df is not None:
    
    # Display Data Head
    st.header("1. Data Overview")
    st.dataframe(df.head(), use_container_width=True)
    
    # Create Filters in the Sidebar
    st.sidebar.header("Data Filters")
    selected_gender = st.sidebar.multiselect(
        "Select Gender:",
        options=df['gender'].unique(),
        default=df['gender'].unique()
    )
    
    # Filter the DataFrame
    df_filtered = df[df['gender'].isin(selected_gender)]
    
    st.subheader(f"Filtered Data: {len(df_filtered)} Records")

    # --- Analysis: Score Distribution ---
    st.header("2. Score Distributions")
    
    # Box plot showing score distribution by gender
    score_column = st.selectbox(
        "Select Score to Visualize:",
        options=['math_score', 'reading_score', 'writing_score']
    )
    
    fig = px.box(
        df_filtered, 
        x="gender", 
        y=score_column, 
        color="gender",
        title=f'Distribution of {score_column.replace("_", " ").title()} by Gender'
    )
    st.plotly_chart(fig, use_container_width=True)

    # --- Analysis: Parental Education vs. Average Scores ---
    st.header("3. Parental Education vs. Average Scores")
    
    avg_scores_by_parent_ed = df_filtered.groupby('parental_level_of_education')[['math_score', 'reading_score', 'writing_score']].mean().reset_index()
    avg_scores_by_parent_ed = avg_scores_by_parent_ed.sort_values(by='math_score', ascending=False)
    
    st.bar_chart(avg_scores_by_parent_ed.set_index('parental_level_of_education'))


# --- Footer ---
st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit and Pandas.")
