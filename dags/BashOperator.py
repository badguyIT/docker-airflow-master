from datetime import datetime
from airflow.models import DAG,Variable
from airflow.operators.bash_operator import BashOperator


default_args={
    'owner':'loy',
    'start_date':datetime(2024,7,30)
}

with DAG(
    dag_id='BashOperator1',
    default_args=default_args,
    schedule_interval=None) as dag:

    start_dag=BashOperator(
        task_id="start_dag",
        bash_command="date"
    )

    start_dag
