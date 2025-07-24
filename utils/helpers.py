"""Utility functions for clipboard operations and text parsing."""

import re
import time
import pyautogui
import pyperclip

from config.constants import LOCAL_DELAY_TIME
from automation.gui_actions import change_tab


def extract_sku_with_context(text_lines: str):
    """Return a list of SKUs with three following context lines."""
    lines = text_lines.split("\n") if isinstance(text_lines, str) else text_lines
    results = []
    for i, line in enumerate(lines):
        sku_match = re.search(r"(?:SKU:\s*)?([A-Z]{3}-[A-Z]{3}-[A-Z]{3}-\d{5})", line)
        if sku_match:
            sku = sku_match.group(1)
            context = []
            remaining = lines[i + 1 :]
            for nxt in remaining:
                stripped = nxt.strip()
                if stripped:
                    context.append(stripped)
                    if len(context) == 3:
                        break
            results.append([sku] + context)
    return results


def copy_customer() -> None:
    """Copy customer name from the active spreadsheet cell."""
    pyautogui.hotkey("ctrl", "c")
    time.sleep(LOCAL_DELAY_TIME)
    for _ in range(2):
        pyautogui.press("left")
        time.sleep(LOCAL_DELAY_TIME)


def copy_id() -> None:
    """Copy ID/reference number from the sheet."""
    pyautogui.hotkey("ctrl", "c")
    time.sleep(LOCAL_DELAY_TIME)
    copied_id = pyperclip.paste()
    print(copied_id)
    pyautogui.press("right")
    time.sleep(LOCAL_DELAY_TIME)


def copy_date() -> None:
    """Copy invoice date from the sheet."""
    pyautogui.hotkey("ctrl", "c")
    time.sleep(LOCAL_DELAY_TIME)
    for _ in range(2):
        pyautogui.press("right")
        time.sleep(LOCAL_DELAY_TIME)


def copy_item_id() -> None:
    """Copy item SKU from the sheet."""
    pyautogui.hotkey("ctrl", "c")
    for _ in range(2):
        pyautogui.press("right")
        time.sleep(LOCAL_DELAY_TIME)


def copy_quantity() -> None:
    """Copy quantity from the sheet."""
    pyautogui.hotkey("ctrl", "c")
    time.sleep(LOCAL_DELAY_TIME)


def copy_value() -> None:
    """Copy unit value from the sheet and paste into the system."""
    for _ in range(2):
        pyautogui.press("right")
        time.sleep(LOCAL_DELAY_TIME)
    pyautogui.hotkey("ctrl", "c")
    change_tab("left")
    item_value = pyperclip.paste()
    pyautogui.write(item_value)
    time.sleep(LOCAL_DELAY_TIME / 2)
    pyautogui.press("tab")
    pyautogui.hotkey("shift", "tab")
    change_tab("right")
    for _ in range(2):
        pyautogui.press("right")
        time.sleep(LOCAL_DELAY_TIME)
    pyautogui.press("down")
    time.sleep(LOCAL_DELAY_TIME)
