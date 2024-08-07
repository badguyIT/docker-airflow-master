from datetime import datetime
from airflow.models import DAG,Variable
from airflow.operators.python_operator import PythonOperator
from bots.PythonHelper import call


default_args={
    'owner':'loy',
    'start_date':datetime(2024,7,7)
}

with DAG(
    dag_id="loy",
    default_args=default_args,
    schedule_interval=None) as dag:

    start_dag=PythonOperator(
        task_id='start_dag',
        python_callable=call
    )

    start_dag

