# Data Pipeline with Airflow: Text to Database Upload
This repository contains a sample data pipeline created using Apache Airflow, designed to convert text data into a CSV file and upload it to a MySQL database.

## Prerequisites
Before running the data pipeline, ensure you have the following components set up:

* Apache Airflow: Install Apache Airflow on your system or server. 

* MySQL Database: Set up a MySQL database where you want to upload the data.

* Python Libraries: Install the required Python libraries using the following command:
`
pip install sqlalchemy
`
`
pip install pandas
`
## Usage
Follow these steps to use and run the data pipeline:

1. Configure the Script: Open the local_txt_to_db_pipeline.py script in a text editor and make the following configurations:

* Update the txt_file_path variable with the path to your source text file.
* Update the csv_file_path variable with the desired path for the generated CSV file.
* Update the db_url variable with your MySQL database connection details.

2. Run the Data Pipeline: Start the Airflow webserver by running the following command in your terminal:

``
airflow webserver -p 8080
``
Access the Airflow UI: Open a web browser and navigate to http://localhost:8080 (replace with your server's address). Here, you can monitor and manage your data pipeline.

Run the DAG: In the Airflow UI, locate the local_txt_to_db_pipeline DAG and trigger the upload_task manually or let the scheduler execute it based on the defined schedule interval.

## Working
This data pipeline performs the following steps:

1. The convert_txt_to_csv_and_upload Python function reads data from the specified text file, converts it to CSV format using pandas, and saves the CSV file to the specified path.

2. The data is then uploaded to the MySQL database using SQLAlchemy, creating a connection to the database and uploading the data as a new table named demo.

3. An Apache Airflow DAG (local_txt_to_db_pipeline) is defined to execute the convert_txt_to_csv_and_upload function using a PythonOperator (upload_task). The DAG's default arguments specify the owner, start date, and other settings.

4. The DAG's schedule interval is set to None, meaning it won't run on a recurring basis, and the catchup is set to False to avoid running old tasks.

5. To run the pipeline, start the Airflow webserver, access the Airflow UI, and trigger the upload_task manually or based on the schedule interval.
