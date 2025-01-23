# gui.py

import tkinter as tk
from tkinter import messagebox
from assets.converter import CurrencyConverter

class CurrencyConverterApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Currency Converter")
        self.root.geometry("300x300")
        self.root.resizable(False,False)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Amount:").pack(pady=5)
        self.entry_amount = tk.Entry(self.root)
        self.entry_amount.pack(pady=5)

        tk.Label(self.root, text="From Currency:").pack(pady=5)
        self.from_currency = tk.StringVar(self.root)
        self.from_currency.set("USD")
        tk.OptionMenu(self.root, self.from_currency, *CurrencyConverter.exchange_rates.keys()).pack(pady=5)

        tk.Label(self.root, text="To Currency:").pack(pady=5)
        self.to_currency = tk.StringVar(self.root)
        self.to_currency.set("GHC")
        tk.OptionMenu(self.root, self.to_currency, *CurrencyConverter.exchange_rates.keys()).pack(pady=5)

        tk.Button(self.root, text="Convert", command=self.convert_currency).pack(pady=20)

        self.label_result = tk.Label(self.root, text="Converted Amount: ")
        self.label_result.pack(pady=5)

    def convert_currency(self):
        try:
            amount = float(self.entry_amount.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            result = CurrencyConverter.convert(amount, from_curr, to_curr)
            self.label_result.config(text=f"Converted Amount: {result:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid amount.")

    def run(self):
        self.root.mainloop()