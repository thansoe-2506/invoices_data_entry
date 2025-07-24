import pyautogui
import time, sys, pyperclip, re

from automation.gui_actions import change_tab
from config.constants import (
    DELAY_TIME,
    PAYMENT_SEARCH_ICON,
    PAYMENT_SEARCH_OPEN,
    PAYMENT_REF_FIELD,
    PAYMENT_SEARCH_BTN,
    PAYMENT_STATUS_START,
    PAYMENT_STATUS_END,
    PAYMENT_ROW,
    PAYMENT_RECORD_BTN,
    PAYMENT_DATE_FIELD,
    PAYMENT_DEPOSIT_FIELD,
    PAYMENT_REF_NO_FIELD,
    PAYMENT_SAVE_BTN,
)
task_numbers = int(sys.argv[1])
payayment_received_date = sys.argv[2]
payment_date = str(payayment_received_date).replace('-', ' ')
deposit_to = 'Cashier'
text = ''
ref_no = ''

def find_status(text):
    # Use a regular expression to find "Draft" or "Paid".  The \b ensures
    # that we match whole words only, avoiding partial matches.
    statuses = re.findall(r"\b(Draft|Paid)\b", text)
    return statuses

def row_found(text):
    rows = re.findall(r"\b(KPG Branch|Confirmed)\b", text)
    return rows


def main():
    for i in reversed(range(5)):
        print(f'Starting in {i+1} seconds...')
        time.sleep(DELAY_TIME)

    for j in range(task_numbers):
        # 1. click search icon
        pyautogui.moveTo(*PAYMENT_SEARCH_ICON)
        pyautogui.click(button='left')
        pyautogui.moveTo(*PAYMENT_SEARCH_OPEN)
        pyautogui.click(button='left')
        time.sleep(DELAY_TIME)

        # 2. click reference text box and triple click
        pyautogui.moveTo(*PAYMENT_REF_FIELD)
        pyautogui.click(button='left')
        pyautogui.tripleClick()
        time.sleep(DELAY_TIME)

        change_tab('right')
        time.sleep(DELAY_TIME/1.5)
        pyautogui.hotkey('ctrl','c')
        ref_no = pyperclip.paste()
        pyautogui.press('right')
        change_tab('left')
        time.sleep(DELAY_TIME/1.5)

        # 3. paste the copied text and click search
        pyautogui.hotkey('ctrl','v')
        time.sleep(DELAY_TIME/1.5)
        pyautogui.moveTo(*PAYMENT_SEARCH_BTN)
        pyautogui.click(button='left')
        time.sleep(DELAY_TIME/1.5)

        # check the row is draft or paid or confirmed
        pyautogui.moveTo(*PAYMENT_STATUS_START)
        pyautogui.dragTo(*PAYMENT_STATUS_END, duration=0.5, button='left')
        pyautogui.hotkey('ctrl','c')
        text = pyperclip.paste()
        found_statuses = find_status(text)

        if found_statuses:
            change_tab('right')
            pyautogui.write('draft or paid')
            time.sleep(DELAY_TIME)
            pyautogui.press('down')
            time.sleep(DELAY_TIME)
            pyautogui.press('left')
            time.sleep(DELAY_TIME)
            change_tab('left')
            continue
        elif not row_found(text):
            change_tab('right')
            pyautogui.write('-')
            time.sleep(DELAY_TIME)
            pyautogui.press('down')
            time.sleep(DELAY_TIME)
            pyautogui.press('left')
            time.sleep(DELAY_TIME)
            change_tab('left')
            # print(row_found)
            continue
        else:
            # 4. click the appeared row
            pyautogui.moveTo(*PAYMENT_ROW)
            pyautogui.click(button='left')
            time.sleep(DELAY_TIME/1.5)

            # 5. click the 'Record Payment'
            pyautogui.moveTo(*PAYMENT_RECORD_BTN)
            pyautogui.click(button='left')
            time.sleep(DELAY_TIME/1.5)

            # 6. click the date box and write the desire date (sys.agrv[2])
            pyautogui.moveTo(*PAYMENT_DATE_FIELD)
            pyautogui.tripleClick()
            time.sleep(DELAY_TIME/1.5)
            pyautogui.write(payment_date)
            pyautogui.press('enter')
            time.sleep(DELAY_TIME/1.5)

            # deposit to 'Cashier'
            pyautogui.moveTo(*PAYMENT_DEPOSIT_FIELD)
            pyautogui.click(button='left')
            time.sleep(DELAY_TIME/1.5)
            pyautogui.write(deposit_to)
            pyautogui.press('enter')
            time.sleep(DELAY_TIME/1.5)

            # paster reference number
            pyautogui.moveTo(*PAYMENT_REF_NO_FIELD)
            pyautogui.tripleClick()
            time.sleep(DELAY_TIME/1.5)

            # change_tab('right')
            # pyautogui.press('left')
            # time.sleep(DELAY_TIME)
            # pyautogui.hotkey('ctrl','c')
            # pyautogui.press('right')
            # time.sleep(DELAY_TIME)
            # change_tab('left')

            pyautogui.write(ref_no)
            time.sleep(DELAY_TIME/1.5)

            # 7. click save button
            pyautogui.moveTo(*PAYMENT_SAVE_BTN)
            pyautogui.click(button='left')
            time.sleep(DELAY_TIME*3)

            change_tab('right')
            pyautogui.write('paid')
            pyautogui.press('enter')
            time.sleep(DELAY_TIME)
            pyautogui.press('left')
            change_tab('left')
            text = ''
            pyautogui.scroll(500)
        text = ''
        print(j+1, ' record payment done!')

        for k in range(3):
            print('DELAY TIME BETWEEN TASKS!', k+1 , 'SECONDS')
            time.sleep(0.9)

      
    
    print('all done!')

if __name__ == "__main__":
    main()

