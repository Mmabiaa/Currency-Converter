# converter.py

class CurrencyConverter:
    exchange_rates = {
        "USD": {"GHC": 15.24, "EUR": 0.92, "GBP": 0.77, "JPY": 118.8, "CFA": 605.32},
        "GHC": {"USD": 1 / 15.24, "EUR": 0.074, "GBP": 0.077, "JPY": 12.8, "CFA": 48.32},
        "EUR": {"USD": 1 / 0.92, "GHC": 0.074, "GBP": 0.85, "JPY": 163.07, "CFA": 655.96},
        "GBP": {"USD": 1 / 0.77, "EUR": 1 / 0.85, "GHC": 1 / 0.063, "JPY": 190.8, "CFA": 767.49},
        "JPY": {"USD": 1 / 109.69, "EUR": 1 / 12, "GBP": 0.0052, "GHC": 1 / 12, "CFA": 4.02},
        "CFA": {"USD": 1 / 605.32, "EUR": 1 / 655.96, "GBP": 1 / 767.49, "JPY": 0.25, "GHC": 1 / 48.27},
    }

    @staticmethod
    def convert(amount: float, from_currency: str, to_currency: str) -> float:
        if from_currency == to_currency:
            return amount
        try:
            rate = CurrencyConverter.exchange_rates[from_currency][to_currency]
            return amount * rate
        except KeyError:
            raise ValueError("Invalid currency conversion.")
