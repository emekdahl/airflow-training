from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta

default_args = {
    'retry': 5,
    'retry_delay': timedelta(minutes=5)
}


def _downloading_data():
    print('hello world')


with DAG(dag_id='simple_dag', default_args=default_args, start_date=datetime(2021, 1, 1), catchup=False, schedule_interval=timedelta(hours=1), max_active_runs=1) as dag:

    task_1 = DummyOperator(
        task_id='task_1'
    )

    downloading_data = PythonOperator(
        task_id='downloading_data',
        python_callable=_downloading_data

    )
