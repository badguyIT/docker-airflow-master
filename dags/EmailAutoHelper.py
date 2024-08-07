from datetime import datetime
from airflow.models import DAG,Variable
from airflow.operator.python_operator import PythonOperator
from bots.EmailHelper import send


default_arg = {
    "owner":"loy",
    "start_date": datetime(2024,8,5)
}

with DAG(
    dag_id="AutosendMail",
    default_arg=default_arg,
    schedule_interval=None) as dag:


    send_email=PythonOperator(
        task_id="send_email",
        python_callable=send
    )

    send_email

