# Interactive CSV & Excel Data Explorer
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://aayush-data-explorer.streamlit.app)


A web application built with Streamlit and Pandas that allows users to upload a CSV or Excel file and perform basic data exploration.

This tool provides a user-friendly interface to quickly get insights from a dataset without writing any code.

## Features

-   **File Upload:** Securely upload CSV and Excel files directly in the browser.
-   **Data Preview:** View the first 10 rows of your dataset in a clean, interactive table.
-   **Summary Statistics:** Instantly generate and display descriptive statistics for all numeric columns.
-   **Data Types:** See the data type for each column.
-   **Interactive Visualization:** Select from multiple chart types (Bar, Line, Scatter) to visualize your data.

## Tech Stack

-   **Streamlit:** For the web application framework and user interface.
-   **Pandas:** For data manipulation and analysis.
-   **OpenPyXL:** For reading Excel files.

## Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/aayush-0131/streamlit-data-explorer.git](https://github.com/aayush-0131/streamlit-data-explorer.git)
    cd csv-explorer
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the application, navigate to the project directory in your terminal and execute the following command:

```bash
streamlit run app.py

Your default web browser will automatically open a new tab with the running application.
