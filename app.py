import streamlit as st
import pandas as pd
# Required for Excel support: pip install openpyxl

# Set the title and a little bit of text for the app
st.title("📊 Interactive CSV & Excel Data Explorer")
st.write("Upload a CSV or Excel file and see some basic data analysis.")

# Create the file uploader widget, accepting both csv and xlsx
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

# This block of code will only run if a file has been uploaded
if uploaded_file is not None:
    try:
        # --- Logic to read either CSV or Excel ---
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file type. Please upload a CSV or XLSX file.")
            st.stop() # Stop the script if the file type is not supported
            
        # --- FIX: Convert 'object' columns to string ---
        # This prevents errors with Streamlit's display library (PyArrow)
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].astype(str)

        st.success("File uploaded successfully! Here's a look at your data.")

        # --- Display Data and Summaries ---
        
        st.header("Data Preview")
        st.dataframe(df.head(10))
        
        st.header("Summary Statistics")
        st.write(df.describe())
        
        st.header("Data Types")
        st.write(df.dtypes)
        
        # --- Interactive Visualization ---
        
        st.header("Visualize Data")
        
        # Get a list of all columns that have numeric data for plotting
        numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        
        if not numeric_columns:
            st.warning("No numeric columns found in the data to plot.")
        else:
            # Add a dropdown to select the chart type
            chart_type = st.selectbox(
                "Select Chart Type:",
                ["Bar Chart (Histogram)", "Line Chart", "Scatter Plot"]
            )

            # Conditional logic for displaying charts
            
            if chart_type == "Bar Chart (Histogram)":
                column_to_plot = st.selectbox("Select a column for the Bar Chart:", numeric_columns)
                st.subheader(f"Bar Chart for {column_to_plot}")
                
                # FIX: Get the counts and convert the index (labels) to strings
                counts = df[column_to_plot].value_counts()
                counts.index = counts.index.astype(str)
                st.bar_chart(counts, use_container_width=True)

            elif chart_type == "Line Chart":
                column_to_plot = st.selectbox("Select a column for the Line Chart:", numeric_columns)
                st.subheader(f"Line Chart for {column_to_plot}")
                st.line_chart(df[column_to_plot], use_container_width=True)

            elif chart_type == "Scatter Plot":
                st.subheader("Scatter Plot to compare two columns")
                x_axis_col = st.selectbox("Select the X-axis column:", numeric_columns)
                y_axis_col = st.selectbox("Select the Y-axis column:", numeric_columns)
                
                st.scatter_chart(df, x=x_axis_col, y=y_axis_col, use_container_width=True)

    except Exception as e:
        st.error(f"An error occurred: {e}")