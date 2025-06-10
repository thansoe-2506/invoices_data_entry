import pyautogui
import time, sys, pyperclip, re

DELAY_TIME = 0.6
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

def change_tab(direction='right'):
    if direction == 'right':
        with pyautogui.hold('ctrl'):
            pyautogui.press('tab')
            time.sleep(DELAY_TIME)
    elif direction == 'left':
        with pyautogui.hold(['ctrl','shift']):
            pyautogui.press('tab')
            time.sleep(DELAY_TIME)

def main():
    for i in reversed(range(5)):
        print(f'Starting in {i+1} seconds...')
        time.sleep(DELAY_TIME)

    for j in range(task_numbers):
        # 1. click search icon
        pyautogui.moveTo(1831,669)
        pyautogui.click(button='left')
        pyautogui.moveTo(1859,669)
        pyautogui.click(button='left')
        time.sleep(DELAY_TIME)

        # 2. click reference text box and triple click
        pyautogui.moveTo(1273,371)
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
        pyautogui.moveTo(377,741)
        pyautogui.click(button='left')
        time.sleep(DELAY_TIME/1.5)

        # check the row is draft or paid or confirmed
        pyautogui.moveTo(13, 649)
        pyautogui.dragTo(165, 822, duration=0.5, button='left')
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
            pyautogui.moveTo(657,737)
            pyautogui.click(button='left')
            time.sleep(DELAY_TIME/1.5)

            # 5. click the 'Record Payment'
            pyautogui.moveTo(763,349)
            pyautogui.click(button='left')
            time.sleep(DELAY_TIME/1.5)

            # 6. click the date box and write the desire date (sys.agrv[2])
            pyautogui.moveTo(1029,405)
            pyautogui.tripleClick()
            time.sleep(DELAY_TIME/1.5)
            pyautogui.write(payment_date)
            pyautogui.press('enter')
            time.sleep(DELAY_TIME/1.5)

            # deposit to 'Cashier'
            pyautogui.moveTo(604,522)
            pyautogui.click(button='left')
            time.sleep(DELAY_TIME/1.5)
            pyautogui.write(deposit_to)
            pyautogui.press('enter')
            time.sleep(DELAY_TIME/1.5)

            # paster reference number
            pyautogui.moveTo(1091,522)
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
            pyautogui.moveTo(534,974)
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

