import requests
from bs4 import BeautifulSoup

def get_price(url):
    response = requests.ge(url)
    soup = BeautifulSoup(response.text, "html.parser")
    price_elemente = sou.find("span", class="a-offscreen")

    if price_element is None:
        return None
    return price_element.text.strip()

## URL Teste
url = "https://www.amazon.com.br/Marcador-Uni-Ball-58-9200-Multicor-Pacote/dp/B07S7K1JHZ"

response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
price_element = soup.find("span", class_="a-offscreen")

if price_element is not None:
    price_text = price_element.text.strip()

    price_text = price_text.replace("R$", "")
    price_text = price_text.replace(".", "")
    price_text = price_text.replace(",", ".")

    price = float(price_text)

    target_price = 160.00

    print(f"Current price: R$ {price:.2f}")
    print(f"Target price: R$ {target_price:.2f}")

    if price <= target_price:
        print("Target price reached!")
    else:
        difference = price - target_price
        print(f"The price is R$ {difference:.2f} above the target.")

else:
    print("Price not found.")