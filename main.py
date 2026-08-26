import sys
print(sys.executable)

import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com.br/Marcador-Uni-Ball-58-9200-Multicor-Pacote/dp/B07S7K1JHZ"

headers = {
  "User-Agent": "Mozilla/5.0"
}

response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

price_element = soup.find("span", class_="a-offscreen")
if price_element is not None:
    print(price_element.text)
else:
    print("Price not found.")