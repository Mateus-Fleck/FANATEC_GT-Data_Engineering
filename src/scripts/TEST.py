import requests

# URL da API
url = "https://api.gt-world-challenge-europe.com/cars"

# Enviar uma solicitação GET para a API
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Extrair os dados JSON da resposta
    data = response.json()

    # Iterar sobre os carros e imprimir seus nomes
    for car in data:
        car_name = car['name']
        print(car_name)
else:
    print("Falha na solicitação. Código de status:", response.status_code)
