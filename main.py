import requests
from bs4 import BeautifulSoup

def get_price(url):
    response = requests.ge(url)
    soup = BeautifulSoup(response.text, "html.parser")
    price_element = soup.find("span", class_="a-offscreen")

    if price_element is None:
        return None
    return price_element.text.strip()

def clean_price(price_text):
    price_text = price_text.replace("R$", "")
    price_text = price_text.replace(".", "")
    price_text = price_text.replace(",", ".")

    return float(price_text)

def check_price(current_price, target_price):
    if price <= target_price:
        print("Target price reached!")
    else:
        difference = price - target_price
        print(f"The price is R$ {difference:.2f} above the target.")

## URL Teste
url = "https://www.amazon.com.br/Marcador-Uni-Ball-58-9200-Multicor-Pacote/dp/B07S7K1JHZ"
target_price = 160.00

price_text = get_price(url)

if price_text is not None:
    price = clean_price(price_text)

    print(f"Current price: R$ {price:.2f}")
    print(f"Target price: R$ {target_price:.2f}")  

else:
    print("Price not found.")