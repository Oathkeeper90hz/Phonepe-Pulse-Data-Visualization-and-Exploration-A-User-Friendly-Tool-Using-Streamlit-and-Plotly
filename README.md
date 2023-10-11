# Phonepe Pulse Data Visualization and Exploration

## Problem Statement

The Phonepe Pulse Github repository contains a substantial amount of data related to various metrics and statistics. The goal of this project is to extract this data, process it to obtain insights, and present it in a user-friendly, visually appealing manner. The solution should encompass the following steps:

1. **Data Extraction**: Utilize scripting to clone the data from the Phonepe Pulse Github repository.

2. **Data Transformation**: Convert the extracted data into a suitable format, perform any necessary cleaning and pre-processing steps.

3. **Data Storage**: Insert the transformed data into a MySQL database for efficient storage and retrieval.

4. **Dashboard Creation**: Develop a live geo-visualization dashboard using Streamlit and Plotly in Python. This dashboard will display the data interactively.

5. **Data Retrieval**: Fetch data from the MySQL database to display it on the dashboard.

6. **User Interaction**: Provide at least 10 different dropdown options for users to select various facts and figures to display on the dashboard.

The solution must prioritize security, efficiency, and user-friendliness. The dashboard should be easily accessible and provide valuable insights and information about the data in the Phonepe Pulse Github repository.

## Repository Structure

Inside the repository, you will find the following components:

1. **Main Code**: The main code for Phonepe Pulse Data Visualization and Exploration is located in the `my_app.py` file, which is located in the parent folder named "phonepe."

2. **Data Files**: The necessary data files, including `phonepe_gif`, `phonepe_logo`, and `states.csv`, should be in the main directory where the source code (`my_app.py`) is located.

3. **Data Processing Scripts**: Inside the "code" folder, you will find two additional subfolders: "json_to_csv" and "text_files." The "json_to_csv" folder contains code for converting JSON files to CSV files. Run these scripts to perform the conversion. After converting the JSON data to CSV files, execute the "null_values.py" script to identify and replace any null values within the CSV files.

4. **SQL Database**: The "sql" folder contains code to insert data into the SQL database in the form of tables. To check the tables and headers in the SQL database after running the data insertion scripts, run the "check_tables_and_headers.py" script.

## Running the Application

Once all the necessary data processing steps are complete, you can run the `my_app.py` script to launch the Streamlit and Plotly-powered visualization and exploration dashboard for Phonepe Pulse data.

We hope this project provides valuable insights and facilitates the exploration of the Phonepe Pulse data. If you have any questions or encounter any issues, please refer to the documentation or contact the project maintainers for assistance.

note= fetch the phonepe pulse repositary link from github using this link https://github.com/PhonePe/pulse save that link in your local pc
change the sql password and database with yours and then give the file path for with respect to you root directory 
add geo.json or shapefiles for the geo visualization 
