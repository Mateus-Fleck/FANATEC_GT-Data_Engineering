# Projeto FANATEC_GT-Data_Engineering

## Objetivo
Este projeto tem como objetivo criar um pipeline de dados utilizando tecnologias modernas de data stack, incluindo SQL, Python, Docker, Astro CLI, Airbyte, DBeaver, PostgreSQL, Airflow e DBT. 
O pipeline será responsável por extrair dados de um link específico usando um web crawler em Python, automatizar o processo com o Airflow, realizar transformações de dados usando o DBT e criar um data warehouse (DW) gratuito com camada de analytics em uma plataforma de nuvem como AWS, Azure ou BigQuery.

## Script Python (Web Crawler)
O script Python para o web crawler será incluído como uma DAG (Directed Acyclic Graph) no Airflow. Ele será responsável por extrair dados do link fornecido e carregá-los em uma área de staging no PostgreSQL.

## Airflow DAGs
As DAGs do Airflow serão definidas no diretório dags/. Elas serão configuradas para executar o script Python do web crawler de forma automatizada e agendada.

## Área de Staging (Bronze Layer)
Os dados extraídos pelo web crawler serão armazenados em uma área de staging no PostgreSQL, representando a camada bronze do pipeline.

## Transformações e Testes com DBT
As transformações de dados serão realizadas usando o DBT dentro do Docker. O DBT será configurado para processar os dados da camada bronze e criar modelos analíticos na camada silver.

## Data Warehouse (DW) com Camada de Analytics
O data warehouse gratuito com camada de analytics será configurado em uma plataforma de nuvem, como AWS, Azure ou BigQuery. Os dados processados pelo DBT serão carregados nesta camada para análise e visualização.
