# Web Scraping com Python 🌐🐍

Este é um simples script em Python para realizar web scraping no site da BBC e extrair os títulos das notícias. O código utiliza as bibliotecas `requests` e `BeautifulSoup` para fazer a requisição HTTP e analisar o HTML da página.

## Como funciona 🚀

1. **Importando Bibliotecas:**
   - `requests`: Para fazer a solicitação HTTP.
   - `BeautifulSoup`: Para analisar o HTML da página.
   - `csv`: Para lidar com arquivos CSV.

```python
import requests
from bs4 import BeautifulSoup
import csv
```

2. **Definindo a URL:**
   - Especifique a URL do site que deseja raspar.

```python
url = "https://www.bbc.com"
```

3. **Fazendo a Solicitação:**
   - Utiliza o `requests` para fazer uma solicitação ao site.

```python
r = requests.get(url)
```

4. **Criando o Objeto BeautifulSoup:**
   - Cria um objeto BeautifulSoup para analisar o HTML da página.

```python
soup = BeautifulSoup(r.text, 'html.parser')
```

5. **Encontrando os Dados:**
   - Utiliza o método `find_all` para extrair os títulos das notícias (h3 com a classe 'media__title').

```python
dados = soup.find_all('h3', class_='media__title')
```

6. **Escrevendo em um Arquivo CSV:**
   - Abre um arquivo CSV chamado 'dados.csv' e escreve os títulos nele.

```python
with open('dados.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for dado in dados:
        writer.writerow([dado.text.strip()])
```

## Executando o Código 🏃‍♂️

1. Certifique-se de ter as bibliotecas necessárias instaladas:

```bash
pip install requests beautifulsoup4
```

2. Execute o script Python.

```bash
python seu_script.py
```

3. Verifique o arquivo 'dados.csv' para os títulos das notícias.

**Observação:** Certifique-se de respeitar os termos de serviço do site que você está raspando.

Divirta-se explorando o mundo do web scraping! 🕵️‍♂️✨
