from airflow import DAG 
from airflow.operators.python import PythonOperator
from datetime import datetime 


def start_number(**context):
    context['ti'].xcom_push(key='current_value', value=10) 

def add_five(**context):
    current_value = context['ti'].xcom_pull(key='current_value', task_ids='start_task')
    new_value = current_value + 5 
    context['ti'].xcom_push(key='current_value', value=new_value) 
    print(f"Add 5: {current_value} + 5 = {new_value}")

def multiple_by_two(**context):
    current_value = context["ti"].xcom_pull(key='current_value', task_ids='add_five_task')
    new_value = current_value * 2 
    context['ti'].xcom_push(key='current_value', value=new_value)
    print(f"Multiply by 2: {current_value} * 2 = {new_value}")
    
def subtract_by_three(**context):
    current_value = context['ti'].xcom_pull(key='current_value', task_ids='multiply_by_two_task')
    new_value = current_value - 3
    context['ti'].xcom_push(key='current_value', value=new_value)
    print(f"Subtract by 3: {current_value} - 3 = {new_value}")
    
def square_number(**context):
    current_value = context['ti'].xcom_pull(key='current_value', task_ids='subtract_by_three_task')
    new_value = current_value ** 2
    print(f"Square the result: {current_value} ** 2 = {new_value}")
    

with DAG(
    dag_id='math_sequence_dag',
    start_date=datetime(2025, 7, 14),
    schedule='@once',
    catchup=False
) as dag:
    
    start_task = PythonOperator(
        task_id='start_task',
        python_callable=start_number
    )
    
    add_five_task = PythonOperator(
        task_id='add_five_task',
        python_callable=add_five
    )
    
    multiply_by_two_task = PythonOperator(
        task_id='multiply_by_two_task',
        python_callable=multiple_by_two
    )
    
    subtract_by_three_task = PythonOperator(
        task_id='subtract_by_three_task',
        python_callable=subtract_by_three
    )
    
    square_task = PythonOperator(
        task_id='square_task',
        python_callable=square_number
    )
    
    start_task >> add_five_task >> multiply_by_two_task >> subtract_by_three_task >> square_task
