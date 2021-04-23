from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator
from airflow.models.baseoperator import chain

from datetime import datetime, timedelta

default_args = {
    'retry': 5,
    'retry_delay': timedelta(minutes=5)
}


def _downloading_data(ti, **kwargs):
    with open('/tmp/my_file.txt', 'w') as f:
        f.write('my_data')
    ti.xcom_push(key='my_key', value=43)


def _checking_data(ti):
    my_xcom = ti.xcom_pull(key='my_key', task_ids=['downloading_data'])
    print(my_xcom)


with DAG(dag_id='simple_dag', default_args=default_args, start_date=datetime(2021, 1, 1), catchup=False, schedule_interval=timedelta(hours=1), max_active_runs=1) as dag:

    downloading_data = PythonOperator(
        task_id='downloading_data',
        python_callable=_downloading_data
    )

    checking_data = PythonOperator(
        task_id='checking_data',
        python_callable=_checking_data
    )

    waiting_for_data = FileSensor(
        task_id='waiting_for_data',
        fs_conn_id='fs-default',
        filepath='my_file.txt',
    )

    processing_data = BashOperator(
        task_id='processing_data',
        bash_command='exit 0'
    )

    chain(downloading_data, checking_data, waiting_for_data, processing_data)
