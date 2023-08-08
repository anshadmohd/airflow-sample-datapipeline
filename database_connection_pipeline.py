from sqlalchemy import create_engine
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd

# Define your DAG's default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 8, 1),
    'depends_on_past': False,
    'retries': 1,
}

# Create the DAG
dag = DAG(
    'local_txt_to_db_pipeline',
    default_args=default_args,
    schedule_interval=None,  # Set your desired schedule interval
    catchup=False,
)

# Define a Python function to convert text to CSV and upload to database
def convert_txt_to_csv_and_upload():
    txt_file_path = '/home/anshad/Downloads/image.txt'  # Replace with your TXT file path
    csv_file_path = '/home/anshad/Downloads/test.csv'  # Replace with your desired CSV file path
    
    # Read the text file and convert it to CSV format
    with open(txt_file_path, 'r') as txt_file:
        lines = txt_file.readlines()
        data = [line.strip().split() for line in lines]
        df = pd.DataFrame(data, columns=['column1', 'column2', 'column3'])
    
    # Save the DataFrame as CSV
    df.to_csv(csv_file_path, index=False)
    
    # Create a database connection using SqlAlchemy
    db_url = "mysql+pymysql://root:password@127.0.0.1:3306/datapipeline"
    engine = create_engine(db_url)
    
    # Upload data to the MySQL database
    df.to_sql('demo', con=engine, if_exists='replace', index=False)

# Define PythonOperator to run the convert_txt_to_csv_and_upload function
upload_task = PythonOperator(
    task_id='upload_task',
    python_callable=convert_txt_to_csv_and_upload,
    dag=dag,
)

# Set the DAG's catchup to False to avoid running old tasks
dag.catchup = False
