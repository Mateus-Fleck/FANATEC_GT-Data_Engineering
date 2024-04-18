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

        # Extraindo os nomes das competições e suas descrições
        competition_info = []
        for option in options:
            if option.text.strip() != 'Meeting':
                # Nome da competição
                competition_name = option.text.strip()
                
                # Descrição do circuito (extraindo do atributo 'value' de cada opção)
                circuit_description = option['value']
                
                # Ano do filtro (extrai os últimos 4 caracteres da URL)
                year_filter = url.split('/')[-2]

                # Adicionando os dados à lista
                competition_info.append({
                    'Nome': competition_name,
                    'Descrição do Circuito': circuit_description,
                    'Ano do Filtro': year_filter
                })

        # Imprimindo as informações das competições
        for info in competition_info:
            print("Nome:", info['Nome'])
            print("Descrição do Circuito:", info['Descrição do Circuito'])
            print("Ano do Filtro:", info['Ano do Filtro'])
            print("-----------------------")

    else:
        print("Elemento select não encontrado.")

else:
    print("Falha ao recuperar a página. Código de status:", response.status_code)
