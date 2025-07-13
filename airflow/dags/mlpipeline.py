from airflow import DAG 
from airflow.operators.python import PythonOperator
from datetime import datetime 

# Define task 1 
def preprocess_data():
    print("Preprocessing Data ...")
    
# Define task 2 
def train_model():
    print("Training Model ....")

# Define task 3 
def evaluate_model():
    print("Evaluate Models ...")
    
    
with DAG(
    dag_id='ml_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule="@weekly",
) as dag:
    
    preprocess = PythonOperator(task_id='preprocess_task', python_callable=preprocess_data)
    train = PythonOperator(task_id='train_task', python_callable=train_model)
    evaluate = PythonOperator(task_id='evaluate_task', python_callable=evaluate_model)
    
    
    ## Set dependencies or Sequence
    preprocess >> train >> evaluate 