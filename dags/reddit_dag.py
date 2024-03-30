import sys
import os
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.redit_pipeline import redit_pipeline
from pipelines.s3_pipeline import s3_pipeline



default_args = {
    'owner' : 'Sid@25',
    'start_date' : datetime(2024, 3, 26)
}

file_suffix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='reddit_data_pipeline',
    default_args=default_args,
    start_date=datetime(2024, 3, 26),
    schedule=None,
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)

#Extraction
extractor = PythonOperator(
    task_id="reddit_extraction",
    python_callable=redit_pipeline,
    op_kwargs = {
        'file_name' : f'reddit_{file_suffix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    dag = dag
)

# S3 load
upload_to_s3 = PythonOperator(
    task_id='s3_upload',
    python_callable=s3_pipeline,
    dag=dag
)


extractor >> upload_to_s3