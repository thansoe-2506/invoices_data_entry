"""High-level GUI interactions using PyAutoGUI."""

from typing import Tuple
import time
import pyautogui
import pyperclip

from config.constants import (
    NEW_INVOICE_BTN,
    CLICK_IN_BLANK,
    CUSTOMER_FIELD,
    CUSTOMER_OPTION,
    CUSTOMER_SELECT,
    REFERENCE_FIELD,
    INVOICE_DATE_FIELD,
    WAREHOUSE_FIELD,
    WAREHOUSE_OPTION,
    SAVE_BTN,
    API_DELAY_TIME,
    DELAY_TIME,
    LOCAL_DELAY_TIME,
)


def click_in_blank(x: int = CLICK_IN_BLANK[0], y: int = CLICK_IN_BLANK[1]) -> None:
    """Click a blank area to remove focus from inputs."""
    pyautogui.moveTo(x, y)
    pyautogui.click(button="left")
    time.sleep(LOCAL_DELAY_TIME)


def change_tab(direction: str = "right") -> None:
    """Switch browser/system tabs."""
    if direction == "right":
        with pyautogui.hold("ctrl"):
            pyautogui.press("tab")
            time.sleep(DELAY_TIME / 2)
    else:
        with pyautogui.hold(["ctrl", "shift"]):
            pyautogui.press("tab")
            time.sleep(DELAY_TIME / 2)


def new_invoice() -> None:
    """Open a new invoice form."""
    pyautogui.moveTo(*NEW_INVOICE_BTN)
    time.sleep(DELAY_TIME)
    pyautogui.click(button="left")
    time.sleep(LOCAL_DELAY_TIME)


def add_customer() -> None:
    """Paste the customer name into the invoice."""
    pyautogui.moveTo(*CUSTOMER_FIELD)
    pyautogui.click(button="left")
    time.sleep(LOCAL_DELAY_TIME)
    pyautogui.click(button="left")
    time.sleep(LOCAL_DELAY_TIME)

    copied_customer = pyperclip.paste()
    if copied_customer.strip() == "KPG C1":
        # Selecting KPG C1 takes a while as it is far down the list
        time.sleep(API_DELAY_TIME)
        pyautogui.moveTo(*CUSTOMER_OPTION)
        pyautogui.click(button="left")
        time.sleep(LOCAL_DELAY_TIME * 2)
    else:
        pyautogui.hotkey("ctrl", "v")
        time.sleep(DELAY_TIME * 6)
        pyautogui.press("enter")
        time.sleep(LOCAL_DELAY_TIME * 3)
        pyautogui.moveTo(*CUSTOMER_SELECT)
        pyautogui.click(button="left")
        time.sleep(LOCAL_DELAY_TIME * 3)


def add_reference() -> None:
    """Add a reference/ID to the invoice from the clipboard."""
    pyautogui.moveTo(*REFERENCE_FIELD)
    pyautogui.click(button="left")
    time.sleep(LOCAL_DELAY_TIME)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(LOCAL_DELAY_TIME)


def invoice_date() -> None:
    """Insert the invoice date from the clipboard."""
    copied_date = pyperclip.paste()
    pyautogui.moveTo(*INVOICE_DATE_FIELD)
    pyautogui.tripleClick()
    time.sleep(DELAY_TIME)
    pyautogui.write(copied_date)
    pyautogui.press("enter")
    time.sleep(LOCAL_DELAY_TIME)
    click_in_blank()


def choose_warehouse() -> None:
    """Select the default warehouse option."""
    pyautogui.moveTo(*WAREHOUSE_FIELD)
    pyautogui.click(button="left")
    time.sleep(LOCAL_DELAY_TIME)
    pyautogui.moveTo(*WAREHOUSE_OPTION)
    pyautogui.click(button="left")
    time.sleep(DELAY_TIME * 4)


def product_details() -> None:
    """Paste a product SKU from the clipboard."""
    pyautogui.press("tab")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(LOCAL_DELAY_TIME * 3)
    pyautogui.press("enter")
    time.sleep(LOCAL_DELAY_TIME)
    for _ in range(2):
        pyautogui.press("tab")
        time.sleep(DELAY_TIME / 2)


def quantity() -> None:
    """Paste the quantity from the clipboard."""
    pyautogui.hotkey("ctrl", "v")
    time.sleep(LOCAL_DELAY_TIME)
    pyautogui.press("tab")
    time.sleep(DELAY_TIME / 2)


def add_new_row() -> None:
    """Add a new item row in the invoice."""
    for _ in range(6):
        pyautogui.press("left")
        time.sleep(LOCAL_DELAY_TIME)

    change_tab("left")
    for _ in range(2):
        pyautogui.press("tab")
        time.sleep(DELAY_TIME)

    pyautogui.hotkey("shift", "enter")
    time.sleep(LOCAL_DELAY_TIME)

    for _ in range(5):
        pyautogui.hotkey("shift", "tab")
        time.sleep(LOCAL_DELAY_TIME)

    pyautogui.hotkey("ctrl", "v")
    time.sleep(LOCAL_DELAY_TIME * 3)
    pyautogui.press("enter")
    time.sleep(LOCAL_DELAY_TIME)
    for _ in range(2):
        pyautogui.press("tab")
        time.sleep(DELAY_TIME / 2)


def save_and_confirm() -> None:
    """Click the save button and wait for the action to complete."""
    pyautogui.moveTo(*SAVE_BTN)
    pyautogui.click(button="left")
    time.sleep(DELAY_TIME * 3)
