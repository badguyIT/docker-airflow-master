from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'loy',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
}

dag = DAG(
    'dca_calculation',
    default_args=default_args,
    description='DAG for data transfer and DCA calculation',
    schedule_interval=None,
)

# Transfer DB to schema
transfer_db = BashOperator(
    task_id='transfer_db',
    bash_command='cd ./dbt_proj && dbt run -s data',
    dag=dag,
)

# Run DCA Calculation
dca_calculation = BashOperator(
    task_id='dca_calculation',
    bash_command='cd ./dbt_proj && dbt run -s dca_calculation',
    dag=dag,
)

# Test DBT
dbt_test = BashOperator(
    task_id='dbt_test',
    bash_command='cd ./dbt_proj && dbt test',
    dag=dag,
)

transfer_db >> dca_calculation >> dbt_test
