## 📋 Automated Invoice and Payment Entry Scripts

This repository contains two Python automation scripts using **PyAutoGUI** to streamline data entry workflows for invoices and payments between Google Sheets and a web-based accounting system.

---

## 🚀 Features

### `invoices_data_entry.py`

* Automates invoice creation for a given number of tasks.
* Copies customer data, dates, product SKUs, quantities, and unit values from Google Sheets.
* Interacts with a web-based invoice system through mouse and keyboard simulation.
* Extracts and transfers SKU-related product information.
* Validates each invoice and logs error states (e.g., “Error Invoice!”) in the Google Sheet if mismatches occur.
* Plays a notification sound on failure for attention.

### `record_payment.py`

* Automates recording of payment entries.
* Checks invoice status (e.g., **Draft**, **Paid**, **Confirmed**) before proceeding.
* Inputs payment date, reference number, and deposit account.
* Updates status in the sheet accordingly (e.g., marks as **paid**, **draft or paid**, or **-** if invoice row not found).

---

## ⚙️ Requirements

* Python 3.x
* `pyautogui`
* `pyperclip`
* `pygame` (for audio feedback)

These libraries are required for all automation scripts and must be installed before running the tools.

Install dependencies:

```bash
pip install pyautogui pyperclip pygame
```

---

## 🧾 Usage

### 1. **Unified CLI**

Run either workflow through `main.py`:

```bash
python main.py invoice <number_of_tasks>
python main.py payment <number_of_tasks> <payment_date>
```

* **`<number_of_tasks>`** – Number of rows to process.
* **`<payment_date>`** – Date in format `YYYY-MM-DD` (only for the payment command).

### 2. **Direct Execution**

The legacy scripts still work individually if preferred:

```bash
python invoices_data_entry.py <number_of_tasks>
python record_payment.py <number_of_tasks> <payment_date>
```

---

## 🖱️ Notes

* Designed for screen resolution and UI coordinates specific to your layout. You may need to update the coordinates in the script (`pyautogui.moveTo(...)`) if your interface differs.
* Ensure Google Sheet is open and selected in a tab to the right of the system window.
* The scripts simulate keyboard and mouse actions; do not interfere with the mouse or keyboard during execution.

---

## 📂 File Structure

```
.
├── main.py                 # Unified command line entry
├── invoices_data_entry.py  # Handles invoice creation
├── record_payment.py       # Handles payment recording
├── automation/             # GUI actions
├── utils/                  # Helper functions
├── config/                 # Coordinates and constants
├── assets/
│   └── confirmation.wav    # Notification sound
└── README.md               # You're here!
```

The `assets` folder holds `confirmation.wav`, which is played on invoice errors. Adjust `config/constants.py` to point elsewhere if you change its location.

---

## 📢 Warning

These scripts control your mouse and keyboard — use them cautiously and test on non-critical data before applying in production environments.

---

## 🙏 Credits

Developed by Than Soe Aung. Designed for internal use to reduce manual entry time and ensure consistency.
