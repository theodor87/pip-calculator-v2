# Pip Calculator v2.0

Upgraded desktop Forex pip & risk calculator built with Python (Tkinter).

This version is an **enhanced upgrade of a basic pip calculator**, extended with proper risk management logic and additional trading inputs.

---

## What’s New in v2.0

Compared to a basic pip calculator (lot × pips × fixed pip value), this version adds:

- ✅ **Currency pair input** (e.g. EURUSD, USDJPY*)
- ✅ **Account balance input**
- ✅ **Risk percentage (%) based position sizing**
- ✅ **Automatic lot size calculation**
- ✅ **Dynamic pip value logic (USD & JPY pairs)**
- ✅ **Error handling for invalid inputs**
- ✅ **Desktop GUI (Tkinter)**

\* USDJPY and other JPY pairs are handled with JPY-specific pip logic.

---

## How It Works

1. Enter:
   - Currency pair
   - Account balance
   - Risk percentage
   - Stop loss in pips
2. The app calculates:
   - Risk amount in USD
   - Pip value per lot
   - Correct position size (lot size)

This follows **risk-based trading principles** commonly used in professional trading and prop firm environments.

---

## Tech Stack

- Python
- Tkinter (Desktop GUI)

---

## Use Case

- Forex risk management
- Position sizing
- Trading education
- Personal trading tools

---

## Notes

This project focuses on **functionality and correctness**, not UI styling.
It is intended as a practical trading utility and a Python learning project.

