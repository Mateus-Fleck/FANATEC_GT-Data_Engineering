from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

# Definindo os argumentos padrão da DAG
default_args = {
    'owner': 'Fleck_Datta_Solutions',
    'depends_on_past': False,
    'start_date': datetime(2023, 6, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Definindo a DAG
with DAG('hello_world_dag', 
         default_args=default_args, 
         description='A primeira DAG que exibe "Hello World"', 
         schedule_interval='@daily',
         catchup=False) as dag:

    # Operadores
    # Define um nó inicial sem funcionalidade real
    start = DummyOperator(task_id='start')

    # Define um operador que executa um comando Bash para imprimir "Hello World"
    hello = BashOperator(task_id='hello', bash_command='echo Hello World')

    # Define um nó final sem funcionalidade real
    end = DummyOperator(task_id='end')

    # Definindo as dependências
    # Define a ordem de execução das tarefas na DAG
    start >> hello >> end
