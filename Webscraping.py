# Importando as bibliotecas necessárias
import requests
from bs4 import BeautifulSoup
import csv

# Definindo a URL do site que você deseja raspar
url = "https://www.bbc.com"

# Fazendo uma solicitação para o site
r = requests.get(url)

# Criando um objeto BeautifulSoup e especificando o analisador
soup = BeautifulSoup(r.text, 'html.parser')

# Encontrando os dados que você deseja raspar
dados = soup.find_all('h3', class_='media__title')

# Abrindo um arquivo CSV e escrevendo os dados raspados nele
with open('dados.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for dado in dados:
        writer.writerow([dado.text.strip()])
