import streamlit as st
import pandas as pd
# Required for Excel support: pip install openpyxl

# Set the page configuration for a wider layout
st.set_page_config(layout="wide")

# --- Sidebar Controls ---

# Add a title and some text to the sidebar
st.sidebar.title("📊 Data Explorer Controls")
st.sidebar.write("Upload a file and select your analysis options.")

# Create the file uploader widget in the sidebar
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["csv", "xlsx"])


# --- Main Page ---

st.title("Interactive CSV & Excel Data Explorer")
st.write("Upload a CSV or Excel file via the sidebar to begin.")

# This block of code will only run if a file has been uploaded
if uploaded_file is not None:
    try:
        # --- Logic to read either CSV or Excel ---
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        
        # --- FIX: Convert 'object' columns to string ---
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].astype(str)

        st.success("File uploaded successfully! Here's your data analysis.")
        
        # --- Display Data and Summaries on the main page ---
        
        st.header("Data Preview")
        st.dataframe(df.head(10))
        
        st.header("Summary Statistics")
        st.write(df.describe())
        
        st.header("Data Types")
        st.write(df.dtypes)
        
        # --- Interactive Visualization moved to the sidebar ---
        
        st.sidebar.header("Visualize Data")
        
        # Get a list of all columns that have numeric data
        numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        
        if not numeric_columns:
            st.sidebar.warning("No numeric columns found to plot.")
        else:
            # Add a dropdown to select the chart type in the sidebar
            chart_type = st.sidebar.selectbox(
                "Select Chart Type:",
                ["Bar Chart (Histogram)", "Line Chart", "Scatter Plot"]
            )

            # Conditional logic for displaying charts on the main page
            st.header("Data Visualization")

            if chart_type == "Bar Chart (Histogram)":
                column_to_plot = st.sidebar.selectbox("Select a column:", numeric_columns)
                st.subheader(f"Bar Chart for {column_to_plot}")
                
                counts = df[column_to_plot].value_counts()
                counts.index = counts.index.astype(str)
                st.bar_chart(counts, use_container_width=True)

            elif chart_type == "Line Chart":
                column_to_plot = st.sidebar.selectbox("Select a column:", numeric_columns)
                st.subheader(f"Line Chart for {column_to_plot}")
                st.line_chart(df[column_to_plot], use_container_width=True)

            elif chart_type == "Scatter Plot":
                st.subheader("Scatter Plot to compare two columns")
                x_axis_col = st.sidebar.selectbox("Select the X-axis:", numeric_columns)
                y_axis_col = st.sidebar.selectbox("Select the Y-axis:", numeric_columns, index=min(1, len(numeric_columns)-1))
                
                st.scatter_chart(df, x=x_axis_col, y=y_axis_col, use_container_width=True)

    except Exception as e:
        st.error(f"An error occurred: {e}")