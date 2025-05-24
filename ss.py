import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self):
        self.rate = self.get_usd_rate()

    def get_usd_rate(self):
        url = "https://bank.gov.ua/ua/markets/exchangerates"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if cols and cols[1].text.strip() == '840':
                return float(cols[5].text.strip().replace(',', '.'))
        raise ValueError("chet ne poluchilos")

    def convert_to_usd(self, amount_uah):
        return round(amount_uah / self.rate, 2)

if __name__ == "__main__":
    converter = CurrencyConverter()
    try:
        amount_uah = float(input("summa v grivnah: "))
        amount_usd = converter.convert_to_usd(amount_uah)
        print(f"{amount_uah} грн = {amount_usd} USD за курсом {converter.rate} грн/USD")
    except ValueError:
        print("vedite summu ok.")
