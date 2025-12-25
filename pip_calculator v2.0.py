import tkinter as tk #UVOZ BIBLIOTEKE -tkinter je standardna Python biblioteka za pravljenje dekstop aplikacija/GUI tj graphic user interface (dugmad, prozori, input polja)
# as tk (umesto da pišemo tkinter.Label, pisaćemo kraće tk.Label)
# root promenljvia koja predstavlja ceo prozor


root = tk.Tk() # bez ovoga nema aplikacije/sve sto se dodaje (label, dugme, input) ide u ovaj prozor
root.title("Pip Calculator v2.0") # postavlja naslov prozora
root.geometry("360x420") # podesavanje velicine prozora (ukoliko se ne unesu dimenzije tkinter sam odredjuje velicinu)


tk.Label(root, text="Pair (e.g. EURUSD):").pack()
pair_entry = tk.Entry(root)
pair_entry.pack()

tk.Label(root, text="Account balance ($):").pack()
balance_entry = tk.Entry(root)
balance_entry.pack()

tk.Label(root, text="Risk (%):").pack()
risk_entry = tk.Entry(root)
risk_entry.pack()


tk.Label(root, text="Pips:").pack()
pips_entry = tk.Entry(root)
pips_entry.pack()

def get_pip_value(pair):
    pair = pair.upper()
    # Non - JPY pairs (EURUSD, GBPUSD...)
    if pair.endswith("USD") and not pair.endswith("JPY"):
        return 10.0
    # JPY pairs (USDJPY, GBPJPY)
    if pair.endswith("JPY"):
        return 1000.0 # bice podeljeno sa cenom ako dodamo price kasnije
    raise ValueError("Unsupported pair")


def calculate():
    try:
        pair = pair_entry.get()
        balance = float(balance_entry.get())
        risk_percent = float(risk_entry.get())
        pips = float(pips_entry.get())

        pip_value = get_pip_value(pair)

        risk_usd = balance * (risk_percent / 100)
        lot = risk_usd / (pips * pip_value)

        result_label.config(
            text = (
                f"Pair: {pair}\n"
                f"Pip value: ${pip_value:.2f}\n"
                f"Risk: ${risk_usd:.2f}\n"
                f"Lot size: {lot:.3f}\n"
                )
         )

    except Exception as e:
        result_label.config(text=f"Error: {e}")

tk.Button(root, text="Calculate", command=calculate).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
