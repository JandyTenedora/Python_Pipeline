from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from app.data_generator import data_generator
from app.data_ingestion import data_ingestion
from app.data_ingestion.normalisers import customer_acitivity_log_normaliser
from airflow.providers.google.cloud.transfers.gcs_to_local import GCSToLocalFilesystemOperator
from app.log_processor import log_processor

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'data_ingestion_dag',
    default_args=default_args,
    description='A DAG for generating, ingesting, normalising data and processing logs',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    generate_data_task = PythonOperator(
        task_id='generate_data',
        python_callable=data_generator,
    )

    ingest_data_task = PythonOperator(
        task_id='ingest_data',
        python_callable=data_ingestion,
    )

    normalise_data_task = PythonOperator(
        task_id='normalise_data',
        python_callable=customer_acitivity_log_normaliser,
    )

    process_logs_task = PythonOperator(
        task_id='process_logs',
        python_callable=log_processor,
    )

    copy_profiles_task = GCSToLocalFilesystemOperator(
        task_id='copy_profiles',
        bucket='your-gcs-bucket-name',
        object_name='path/to/profiles.yml',
        filename='/home/airflow/gcs/data/profiles.yml',
    )

    dbt_run_task = BashOperator(
        task_id='dbt_run',
        bash_command='dbt run --profiles-dir /home/airflow/gcs/data',
    )

    dbt_test_task = BashOperator(
        task_id='dbt_test',
        bash_command='dbt test --profiles-dir /home/airflow/gcs/data',
    )

    generate_data_task >> ingest_data_task >> normalise_data_task >> process_logs_task