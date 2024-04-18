import requests
from bs4 import BeautifulSoup

# URL da página a ser raspada
url = "https://api.gt-world-challenge-europe.com/results/2023/"

# Fazendo a solicitação HTTP
response = requests.get(url)

# Verificando se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Analisando o conteúdo HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrando o elemento select com o ID 'filter_meeting_id'
    select_element = soup.find('select', id='filter_meeting_id')

    # Verificando se o elemento select foi encontrado
    if select_element:
        # Encontrando todas as opções dentro do elemento select
        options = select_element.find_all('option')

        # Extraindo os nomes das competições das opções
        competition_names = [option.text.strip() for option in options if option.text.strip() != 'Meeting']

        # Imprimindo os nomes das competições
        for name in competition_names:
            print(name)

    else:
        print("Elemento select não encontrado.")

else:
    print("Falha ao recuperar a página. Código de status:", response.status_code)
