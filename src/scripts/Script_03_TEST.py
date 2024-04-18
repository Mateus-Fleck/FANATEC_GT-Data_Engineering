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

    # Encontrando a tabela de resultados
    results_table = soup.find('table', class_='season')

    # Verificando se a tabela foi encontrada
    if results_table:
        # Encontrando todas as linhas da tabela
        rows = results_table.find_all('tr')

        # Iterando sobre as linhas da tabela
        for row in rows:
            # Extraindo as células da linha
            cells = row.find_all('td')
            # Verificando se é uma linha de dados válida
            if len(cells) > 0:
                # Extraindo os dados das células
                race = cells[0].text.strip()
                series = cells[1].text.strip()
                car_number = cells[2].text.strip()
                team = cells[3].text.strip()
                car = cells[4].text.strip()
                time = cells[5].text.strip()
                laps = cells[6].text.strip()

                # Imprimindo os dados
                print("Race:", race)
                print("Series:", series)
                print("Car #:", car_number)
                print("Team:", team)
                print("Car:", car)
                print("Time:", time)
                print("Laps:", laps)
                print("-----------------------")

    else:
        print("Tabela de resultados não encontrada na página.")

else:
    print("Falha ao recuperar a página. Código de status:", response.status_code)
