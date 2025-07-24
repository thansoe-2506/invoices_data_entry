"""Invoice creation workflow using GUI automation."""

from __future__ import annotations

import sys
import time
import pygame
import pyautogui
import pyperclip

from automation import gui_actions as gui
from utils import helpers
from config import constants as C

pygame.mixer.init()
pygame.mixer.music.load(str(C.SOUND_PATH))


def process_invoice() -> None:
    """Handle the steps required to create a single invoice."""
    # copy customer name
    gui.change_tab("right")
    helpers.copy_customer()
    gui.change_tab("left")
    gui.add_customer()

    # reference/ID
    gui.change_tab("right")
    helpers.copy_id()
    gui.change_tab("left")
    gui.add_reference()

    # invoice date
    gui.change_tab("right")
    helpers.copy_date()
    gui.change_tab("left")
    gui.invoice_date()

    # scroll and choose warehouse
    pyautogui.scroll(-500)
    gui.choose_warehouse()

    # product details and quantity
    gui.change_tab("right")
    helpers.copy_item_id()
    gui.change_tab("left")
    gui.product_details()

    gui.change_tab("right")
    helpers.copy_quantity()
    gui.change_tab("left")
    gui.quantity()

    gui.change_tab("right")
    helpers.copy_value()
    gui.change_tab("left")

    # check if invoice has multiple rows
    gui.change_tab("right")
    pyautogui.hotkey("ctrl", "c")
    copied_text = pyperclip.paste()
    while copied_text.strip() == "-":
        gui.add_new_row()
        pyautogui.hotkey("ctrl", "c")
        copied_text = pyperclip.paste()
    for _ in range(7):
        pyautogui.press("left")
        time.sleep(C.LOCAL_DELAY_TIME)
    gui.change_tab("left")

    # extract sku data
    pyautogui.scroll(4000)
    pyautogui.moveTo(378, 907)
    pyautogui.mouseDown(button="left")
    pyautogui.moveTo(1887, 907, duration=1)
    pyautogui.scroll(-3500)
    pyautogui.mouseUp(button="left")

    pyautogui.hotkey("ctrl", "c")
    pyautogui.click(button="left")
    time.sleep(0.5)
    copied_text = pyperclip.paste()
    sku_data = helpers.extract_sku_with_context(copied_text)

    gui.change_tab("right")
    pyautogui.hotkey("ctrl", "right")
    for _ in range(4):
        pyautogui.press("right")
        time.sleep(C.LOCAL_DELAY_TIME)
    for _ in range(len(sku_data)):
        pyautogui.press("up")
        time.sleep(C.LOCAL_DELAY_TIME)
    for entry in sku_data:
        pyperclip.copy((entry[0], entry[1], entry[2], entry[3]))
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("down")
        time.sleep(0.2)
    for _ in range(2):
        pyautogui.hotkey("ctrl", "left")
    for _ in range(4):
        pyautogui.press("right")
        time.sleep(C.LOCAL_DELAY_TIME)
    gui.change_tab("left")

    gui.save_and_confirm()

    # check header to ensure invoice saved
    pyautogui.moveTo(*C.HEADER_FIELD)
    pyautogui.tripleClick()
    pyautogui.hotkey("ctrl", "c")
    header = pyperclip.paste()
    if header.strip() == "New Invoice":
        pyautogui.moveTo(*C.INVALID_CLOSE_BTN)
        pyautogui.click(button="left")
        time.sleep(C.DELAY_TIME * 5)
        gui.change_tab("right")
        pyautogui.press("up")
        time.sleep(C.LOCAL_DELAY_TIME)
        pyautogui.press("right")
        time.sleep(C.LOCAL_DELAY_TIME)
        pyautogui.hotkey("ctrl", "right")
        time.sleep(C.LOCAL_DELAY_TIME)
        pyautogui.press("right")
        time.sleep(C.LOCAL_DELAY_TIME)
        pyautogui.write("Error Invoice!")
        pygame.mixer.music.play()
        pyautogui.hotkey("ctrl", "left")
        time.sleep(C.LOCAL_DELAY_TIME)
        pyautogui.press("down")
        time.sleep(C.LOCAL_DELAY_TIME)
        for _ in range(4):
            pyautogui.press("right")
            time.sleep(C.LOCAL_DELAY_TIME)
        gui.change_tab("left")


def main(task_numbers: int) -> None:
    """Run the invoice automation for a number of tasks."""
    for i in reversed(range(5)):
        print(f"Starting in {i+1} seconds...")
        time.sleep(0.9)
    for _ in range(task_numbers):
        gui.new_invoice()
        process_invoice()
        pyautogui.hotkey("alt", "tab")
        for k in range(3):
            print("DELAY TIME BETWEEN TASKS!", k + 1, "SECONDS")
            time.sleep(0.9)
        pyautogui.hotkey("alt", "tab")
    print("ALL DONE!!!!")


if __name__ == "__main__":
    main(int(sys.argv[1]))
