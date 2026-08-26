import requests
from bs4 import BeautifulSoup

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
        print("The price is still above the target.")

else:
    print("Price not found.")