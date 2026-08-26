# Price Tracker

A simple Python project that tracks product prices using web scraping.

The goal of this project is to practice Python fundamentals, HTTP requests, HTML parsing, data handling, and project organization while building a useful real-world application.

## Features

- Fetch product pages from the web
- Extract product prices
- Compare the current price with a target price
- Display whether the product has reached the desired value

## Technologies

- Python 3Python: Select Interpreter
- Requests
- Beautiful Soup

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/price-tracker.git
```

Enter the project directory:

```bash
cd price-tracker
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

The program will ask for the product URL and the desired price.

Example:

```text
=== PRICE TRACKER ===

Product URL: https://example.com/product
Target price: 1200

Current price: R$ 1,399.00
Target price: R$ 1,200.00

The product is still R$ 199.00 above the target price.
```

## Project Structure

```text
price-tracker/
│
├── main.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Future Improvements

- Track multiple products
- Store price history
- Add automatic price checks
- Send notifications when a product reaches the target price
- Add better error handling
- Support multiple online stores
- Store data using JSON or SQLite
- Add a graphical interface

## Learning Goals

This project was created to practice:

- Python functions
- HTTP requests
- Web scraping
- HTML parsing
- Error handling
- Data processing
- Code organization

## Disclaimer

This project is intended for educational purposes. Websites may have different terms of service and restrictions regarding automated access or web scraping.

## License

This project is licensed under the MIT License.
