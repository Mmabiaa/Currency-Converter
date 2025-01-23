import requests

class CurrencyConverter:
    # API details
    url = "https://api.apilayer.com/exchangerates_data/latest"
    headers = {
        "apikey": "<your_api_key>"
    }

    exchange_rates = {}

    @classmethod
    def fetch_exchange_rates(cls, base_currency, target_currencies):
        symbols = ",".join(target_currencies)
        full_url = f"{cls.url}?symbols={symbols}&base={base_currency}"
        response = requests.get(full_url, headers=cls.headers)
        data = response.json()
        rates = data.get("rates", {})
        

        cls.exchange_rates[base_currency] = {currency: rates[currency] for currency in target_currencies}
        for target_currency in target_currencies:
            target_url = f"{cls.url}?symbols={symbols}&base={target_currency}"
            target_response = requests.get(target_url, headers=cls.headers)
            target_data = target_response.json()
            target_rates = target_data.get("rates", {})
            cls.exchange_rates[target_currency] = {currency: target_rates[currency] for currency in target_currencies if currency != target_currency}


    @staticmethod
    def convert(amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        rate = CurrencyConverter.exchange_rates[from_currency][to_currency]
        return round(amount * rate, 4)