import tkinter as tk
from tkinter import messagebox

def convert_currency():
    try:
        amount = float(entry_amount.get())
        if from_currency.get() == "USD":
            if to_currency.get() == "GHC":
                result = 15.24 * amount
            elif to_currency.get() == "EUR":
                result = 0.92 * amount
            elif to_currency.get() == "GBP":
                result = 0.77 * amount
            elif to_currency.get() == "JPY":
                result = 118.8 * amount
            elif to_currency.get() == "CFA":
                result = 605.32 * amount
            else:
                result = amount
        elif from_currency.get() == "GHC":
            if to_currency.get() == "USD":
                result = amount / 15.24
            elif to_currency.get() == "EUR":
                result = 0.074 * amount
            elif to_currency.get() == "GBP":
                result = 0.077 * amount
            elif to_currency.get() == "JPY":
                result = 12.8 * amount
            elif to_currency.get() == "CFA":
                result = 48.32 * amount
            else:
                result = amount
        elif from_currency.get() == "EUR":
            if to_currency.get() == "USD":
                result = amount / 0.92
            elif to_currency.get() == "GHC":
                result = amount / 0.074
            elif to_currency.get() == "GBP":
                result = 0.85 * amount
            elif to_currency.get() == "JPY":
                result = 163.07 * amount
            elif to_currency.get() == "CFA":
                result = 655.96 * amount
            else:
                result = amount
        elif from_currency.get() == "GBP":
            if to_currency.get() == "USD":
                result = amount / 0.77
            elif to_currency.get() == "EUR":
                result = amount / 0.85
            elif to_currency.get() == "GHC":
                result = amount / 0.063
            elif to_currency.get() == "JPY":
                result = 190.8 * amount
            elif to_currency.get() == "CFA":
                result = 767.49 * amount
            else:
                result = amount
        elif from_currency.get() == "JPY":
            if to_currency.get() == "USD":
                result = amount / 109.69
            elif to_currency.get() == "EUR":
                result = amount / 12
            elif to_currency.get() == "GBP":
                result = 0.0052 * amount
            elif to_currency.get() == "GHC":
                result = amount / 12
            elif to_currency.get() == "CFA":
                result = 4.02 * amount
            else:
                result = amount
        elif from_currency.get() == "CFA":
            if to_currency.get() == "USD":
                result = amount / 605.32
            elif to_currency.get() == "EUR":
                result = amount / 655.96
            elif to_currency.get() == "GBP":
                result = amount / 767.49
            elif to_currency.get() == "JPY":
                result = 0.25 * amount
            elif to_currency.get() == "GHC":
                result = amount / 48.27
            else:
                result = amount
        else:
            result = amount

        label_result.config(text=f"Converted Amount: {result:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount.")

def create_currency_converter():
    global entry_amount, from_currency, to_currency, label_result

    root = tk.Tk()
    root.title("Let's Convert Some Currencies")
    root.geometry("300x300")

    tk.Label(root, text="Amount:").pack(pady=5)
    entry_amount = tk.Entry(root)
    entry_amount.pack(pady=5)

    tk.Label(root, text="From Currency:").pack(pady=5)
    from_currency = tk.StringVar(root)
    from_currency.set("USD")
    tk.OptionMenu(root, from_currency, "USD", "GHC", "EUR", "GBP", "JPY", "CFA").pack(pady=5)

    tk.Label(root, text="To Currency:").pack(pady=5)
    to_currency = tk.StringVar(root)
    to_currency.set("GHC")
    tk.OptionMenu(root, to_currency, "USD", "GHC", "EUR", "GBP", "JPY", "CFA").pack(pady=5)

    tk.Button(root, text="Convert", command=convert_currency).pack(pady=20)

    label_result = tk.Label(root, text="Converted Amount: ")
    label_result.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_currency_converter()