from bs4 import BeautifulSoup

html_content = """
<ul class="link-cards__list-items">

    <li class="link-cards__list-item">
        <a class="link-cards__link" href="/car/150/aston-martin-vantage-amr-gt3">
            <div class="link-cards__image-container">
                <div class="link-cards__image-inner-container image-type--logo">
                    <img class="link-cards__image" src="https://api.gt-world-challenge-europe.com/timthumb.php?w=400&src=%2Fimages%2Fcompetitors%2Flogo_144.png" width="335" height="224" alt="Aston Martin Vantage AMR GT3 EVO">
                </div>
            </div>
            <div class="link-cards__text-container">
                <h3 class="link-cards__header">Aston Martin Vantage AMR GT3 EVO</h3>
            </div>
        </a>
    </li>

    <!-- Outros elementos li -->

</ul>
"""

# Criando o objeto BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Encontrando todos os elementos li dentro da classe link-cards__list-items
car_items = soup.find_all('li', class_='link-cards__list-item')

# Iterando sobre os elementos li para extrair nome do carro e URL da imagem da marca
for car_item in car_items:
    car_name = car_item.find('h3', class_='link-cards__header').text.strip()
    logo_url = car_item.find('img', class_='link-cards__image')['src']
    print("Nome do Carro:", car_name)
    print("URL da Imagem:", logo_url)
    print()
