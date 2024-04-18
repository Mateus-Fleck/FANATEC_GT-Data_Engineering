import requests
from bs4 import BeautifulSoup

# URL da página que contém informações sobre os carros
url = "https://api.gt-world-challenge-europe.com/cars"

# Fazendo a solicitação HTTP
response = requests.get(url)

# Verificando se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Analisando o conteúdo HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrando todos os elementos de link que contêm informações sobre os carros
    car_links = soup.find_all('a', class_='sponsors__list-link')

    # Extraindo os nomes dos carros dos links
    car_names = [link.text.strip() for link in car_links]

    # Agrupando os carros por nome e adicionando o ano '2024'
    unique_car_names = set(car_names)

    # Imprimindo o resultado formatado
    print("2023")
    print("CARS")
    for name in unique_car_names:
        print(name)

else:
    print("Falha ao recuperar os dados. Código de status:", response.status_code)

