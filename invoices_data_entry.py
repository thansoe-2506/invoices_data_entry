import sys, re
import pyautogui
import time
import pyperclip
import pygame
 
pygame.mixer.init()
pygame.mixer.music.load("source/mixkit-confirmation-tone-2867.wav")  # Can also use .wav

API_DELAY_TIME = 4 # based on the internet connection
DELAY_TIME = 0.6
LOCAL_DELAY_TIME = 0.3

task_numbers = int(sys.argv[1])

def extract_sku_with_context(text_lines):
    # Split text into lines
    lines = text_lines.split('\n') if isinstance(text_lines, str) else text_lines
    results = []
    
    for i, line in enumerate(lines):
        # Find SKU pattern (with optional "SKU:" prefix)
        sku_match = re.search(r'(?:SKU:\s*)?([A-Z]{3}-[A-Z]{3}-[A-Z]{3}-\d{5})', line)
        if sku_match:
            sku = sku_match.group(1)
            context_lines = []
            
            # Get next lines after current line
            remaining_lines = lines[i+1:]
            
            # Collect next 3 non-empty lines
            for next_line in remaining_lines:
                stripped = next_line.strip()
                if stripped:
                    context_lines.append(stripped)
                    if len(context_lines) == 3:
                        break
            
            # Add to results (SKU + context lines)
            results.append([sku] + context_lines)
    
    return results

def click_in_blank(a=1884,b=410):
    pyautogui.moveTo(a,b)
    pyautogui.click(button='left')
    time.sleep(LOCAL_DELAY_TIME)

def change_tab(direction='right'):
    if direction == 'right':
        with pyautogui.hold('ctrl'):
            pyautogui.press('tab')
            time.sleep(DELAY_TIME/2)
    elif direction == 'left':
        with pyautogui.hold(['ctrl','shift']):
            pyautogui.press('tab')
            time.sleep(DELAY_TIME/2)

def new_invoice():
    pyautogui.moveTo(1835,259)
    time.sleep(DELAY_TIME)

    pyautogui.click(button='left')
    time.sleep(LOCAL_DELAY_TIME)

def add_customer():
    pyautogui.moveTo(792,364)
    pyautogui.click(button='left')
    time.sleep(LOCAL_DELAY_TIME)

    pyautogui.click(button='left')
    time.sleep(LOCAL_DELAY_TIME)

    # check the customer is KPG C1 or else, cuz KPG C1 is over 1300 row

    copied_customer = pyperclip.paste()
    if copied_customer.strip() == 'KPG C1':
        time.sleep(API_DELAY_TIME) # delay to appear customer name
        pyautogui.moveTo(784,647)
        pyautogui.click(button='left')
        time.sleep(LOCAL_DELAY_TIME*2)
    else:
        pyautogui.hotkey("ctrl", "v")
        time.sleep(DELAY_TIME*6)
    
        pyautogui.press('enter')
        time.sleep(LOCAL_DELAY_TIME*3) # delay to click customer name

        pyautogui.moveTo(738, 568)
        pyautogui.click(button='left')
        time.sleep(LOCAL_DELAY_TIME*3)

    
def copy_customer():
    pyautogui.hotkey("ctrl", "c")
    time.sleep(LOCAL_DELAY_TIME)

    for _ in range(2):
        pyautogui.press('left')
        time.sleep(LOCAL_DELAY_TIME)

def add_reference():
    pyautogui.moveTo(1531,526)
    pyautogui.click(button='left')
    time.sleep(LOCAL_DELAY_TIME)

    pyautogui.hotkey("ctrl", "v")
    time.sleep(LOCAL_DELAY_TIME)


def copy_id():
    pyautogui.hotkey("ctrl", "c")
    time.sleep(LOCAL_DELAY_TIME)

    copied_id = pyperclip.paste()
    print(copied_id)

    pyautogui.press('right')
    time.sleep(LOCAL_DELAY_TIME)

def copy_date():
    pyautogui.hotkey('ctrl','c')
    time.sleep(LOCAL_DELAY_TIME)

    for _ in range(2):
        pyautogui.press('right')
        time.sleep(LOCAL_DELAY_TIME)

def invoice_date():
    copied_date = pyperclip.paste()

    pyautogui.moveTo(791, 607)
    pyautogui.tripleClick()
    time.sleep(DELAY_TIME)

    pyautogui.write(copied_date)
    pyautogui.press('enter')
    time.sleep(LOCAL_DELAY_TIME)

    click_in_blank()


def choose_warehouse():
    pyautogui.moveTo(608, 430)
    pyautogui.click(button='left')
    time.sleep(LOCAL_DELAY_TIME)

    pyautogui.moveTo(602,529)
    pyautogui.click(button='left')
    time.sleep(DELAY_TIME*4)

def product_details():
    pyautogui.press('tab')

    pyautogui.hotkey('ctrl','v')
    time.sleep(LOCAL_DELAY_TIME*3)

    pyautogui.press('enter')
    time.sleep(LOCAL_DELAY_TIME)
    for _ in range(2):
        pyautogui.press('tab')
        time.sleep(DELAY_TIME/2)

def copy_item_id():
    pyautogui.hotkey('ctrl','c')

    for _ in range(2):
        pyautogui.press('right')
        time.sleep(LOCAL_DELAY_TIME)


def copy_quantity():
    pyautogui.hotkey('ctrl','c')
    time.sleep(LOCAL_DELAY_TIME)


def copy_value():
    for _ in range(2):
        pyautogui.press('right')
        time.sleep(LOCAL_DELAY_TIME)
    pyautogui.hotkey('ctrl','c')

    change_tab('left')

    # paste item unit value
    # pyautogui.hotkey('ctrl','v')
    item_value = pyperclip.paste()
    pyautogui.write(item_value)
    time.sleep(LOCAL_DELAY_TIME/2)
    
    pyautogui.press('tab')
    pyautogui.hotkey('shift','tab')
    # done paste item unit value


    change_tab('right')

    for _ in range(2):
        pyautogui.press('right')
        time.sleep(LOCAL_DELAY_TIME)

    pyautogui.press('down')
    time.sleep(LOCAL_DELAY_TIME)


def quantity():
    pyautogui.hotkey('ctrl','v')
    time.sleep(LOCAL_DELAY_TIME)

    pyautogui.press('tab')
    time.sleep(DELAY_TIME/2)
    # pyautogui.hotkey('shift','tab')

    # click_in_blank(1139,634) #first item, product detail


def click_cancel():
    pyautogui.moveTo(764,969)
    pyautogui.click(button='left')
    time.sleep(LOCAL_DELAY_TIME)

def add_new_row():
    for _ in range(6):
        pyautogui.press('left')
        time.sleep(LOCAL_DELAY_TIME)

    copy_item_id()

    change_tab('left')

    # move to add new row button
    for _ in range(2):
        pyautogui.press('tab')
        time.sleep(DELAY_TIME)

    # click add new row button
    pyautogui.hotkey('shift','enter')
    time.sleep(LOCAL_DELAY_TIME)

    # got to add item code
    for _ in range(5):
        pyautogui.hotkey('shift','tab')
        time.sleep(LOCAL_DELAY_TIME)

    # paste item code
    pyautogui.hotkey('ctrl','v')
    time.sleep(LOCAL_DELAY_TIME*3)

    # choose item code
    pyautogui.press('enter')
    time.sleep(LOCAL_DELAY_TIME)

    # got to add quantity
    for _ in range(2):
        pyautogui.press('tab')
        time.sleep(DELAY_TIME/2)

    change_tab('right')

    pyautogui.hotkey('ctrl','c')
    # pyautogui.press('')

    change_tab('left')
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('tab')
    change_tab('right')

    for _ in range(2):
        pyautogui.press('right')
        time.sleep(LOCAL_DELAY_TIME)

    pyautogui.hotkey('ctrl','c')

    change_tab('left')
    # paste item unit value
    # pyautogui.hotkey('ctrl','v')

    item_value = pyperclip.paste()
    pyautogui.write(item_value)
    time.sleep(LOCAL_DELAY_TIME/2)

    pyautogui.press('tab')
    pyautogui.hotkey('shift','tab')
    # done paste item unit value
    change_tab('right')

    #copy unit

    for _ in range(2):
        pyautogui.press('right')
        time.sleep(LOCAL_DELAY_TIME)

    pyautogui.press('down')
    time.sleep(LOCAL_DELAY_TIME)

    change_tab('left')

    # paste the quantity, second item in same invoice
    # pyautogui.hotkey('ctrl','v')
    pyautogui.press('tab')
    time.sleep(LOCAL_DELAY_TIME)
    pyautogui.hotkey('shift','tab')
    time.sleep(LOCAL_DELAY_TIME)
    # click_in_blank(1172,839) # second item, product details

    change_tab('right')
    
def save_and_confirm():
    pyautogui.moveTo(612,975)
    pyautogui.click(button='left')
    time.sleep(DELAY_TIME*3)


def main():
    for i in reversed(range(5)):
        print('there is first time delay for', i+1 ,' seconds!')
        time.sleep(0.9)
    for j in range(task_numbers):
        # first of all, click new invoice button
        new_invoice()

        # copy customer name from google sheet and add customer name
        change_tab('right')
        copy_customer() # action in google sheet
        print('customer copied from google sheets!')
        change_tab('left')

        add_customer() # action in system
        print('customer added in system!')

        change_tab('right')
        copy_id() # action in google sheet
        print('copied id/reference from google sheets!')
        change_tab('left')

        add_reference() # action in system
        print('id/reference added in system!')

        change_tab('right')
        copy_date() 
        print('date copied from google sheets!')
        change_tab('left')

        invoice_date() # action in system, adding date
        time.sleep(LOCAL_DELAY_TIME)
        print('date added!')

        # scroll down about one page
        pyautogui.scroll(-500)

        # choose warehouse, alway KPG - Sale Center 
        choose_warehouse()
        print('choose warehouse!')

        # first time product details, don't need to click 'add new row', use tab key instead of mouse click
        change_tab('right')
        copy_item_id() # action in google sheet
        print('adding product details...')
        change_tab('left')

        product_details() # action in system, adding product detals
        print('product details added!')
        
        change_tab('right')
        copy_quantity() # action in google sheet
        change_tab('left')
        print('quantity copied!')

        quantity() # action in system, adding quantity, maybe need to click empty space
        print('quantity checked!')

        change_tab('right')
        copy_value()
        change_tab('left')

        # if the invoice have two or more items, need to click add_new_row()
        change_tab('right')
        
        pyautogui.hotkey('ctrl','c')
        copied_text = pyperclip.paste()
        # print('|',copied_text,'|')

        while copied_text.strip() == '-':
            add_new_row()

            pyautogui.hotkey('ctrl','c')
            copied_text = pyperclip.paste()
            print('adding new row..')

        # GOOGLE SHEET, MOVE CELL TO CUSTOMER NAME
        for _ in range(7):
            pyautogui.press('left')
            time.sleep(LOCAL_DELAY_TIME)
        change_tab('left')

        # extract sku data
        pyautogui.scroll(4000)

        pyautogui.moveTo(378, 907)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(1887, 907, duration=1)
        pyautogui.scroll(-3500)
        pyautogui.mouseUp(button='left')

        pyautogui.hotkey('ctrl', 'c')
        pyautogui.click(button='left')
        time.sleep(0.5)  # Add small delay for clipboard to update
        copied_text = pyperclip.paste()

        # print("Copied text:")
        # print(copied_text)

        # Process the text directly (no need to split/strip here)
        sku_data = extract_sku_with_context(copied_text)
        print(len(sku_data))
        
        change_tab('right')
        pyautogui.hotkey('ctrl','right')
        for _ in range(4):
            pyautogui.press('right')
            time.sleep(LOCAL_DELAY_TIME)
        for _ in range(len(sku_data)):
            pyautogui.press('up')
            time.sleep(0.2)
        # change_tab('left')
        
        print("\nExtracted SKUs with context:")
        # change_tab('right')
        for entry in sku_data:
            print(entry[0],entry[1], entry[2], entry[3])
            temp_text = entry[0],entry[1], entry[2], entry[3]
            pyperclip.copy(temp_text)
            pyautogui.hotkey('ctrl','v')
            pyautogui.press('down')
            time.sleep(0.2)
        # change_tab('left')

        # change_tab('right')
        for _ in range(2): pyautogui.hotkey('ctrl','left')
        for _ in range(4):
            pyautogui.press('right')
            time.sleep(LOCAL_DELAY_TIME)
        change_tab('left')
        
        # end extract sku data

        pyautogui.hotkey('alt','tab')
        time.sleep(DELAY_TIME/2)
        for k in range(3):
            print('DELAY TIME BETWEEN TASKS!', k+1 , 'SECONDS')
            time.sleep(0.9)
        pyautogui.hotkey('alt','tab')

        save_and_confirm()

        # before ending a task, check task should skip or not
        # if the header is still New Invoices, should skip the task and add note in google sheet
        # if the header is Invoices, the task shall continue

        # check header
        pyautogui.moveTo(441,264)
        pyautogui.tripleClick()
        pyautogui.hotkey('ctrl','c')
        header = pyperclip.paste()
        print(header)

        if header.strip() == 'New Invoice':
            pyautogui.moveTo(1867,260)
            pyautogui.click(button='left')
            time.sleep(DELAY_TIME*5)

            print('Invoice is not vlaid, Quantity Not Match!')
            
            change_tab('right')
            pyautogui.press('up')
            time.sleep(LOCAL_DELAY_TIME)
            pyautogui.press('right')
            time.sleep(LOCAL_DELAY_TIME)
            pyautogui.hotkey('ctrl','right')
            time.sleep(LOCAL_DELAY_TIME)
            pyautogui.press('right')
            time.sleep(LOCAL_DELAY_TIME)
            pyautogui.write('Error Invoice!')

            # play a notification sound when the quantity not match
            pygame.mixer.music.play()
            
            pyautogui.hotkey('ctrl','left')
            time.sleep(LOCAL_DELAY_TIME)
            pyautogui.press('down')
            time.sleep(LOCAL_DELAY_TIME)
            for _ in range(4): 
                pyautogui.press('right')
                time.sleep(LOCAL_DELAY_TIME)
            change_tab('left')

            pyautogui.hotkey('alt','tab')
            time.sleep(DELAY_TIME/2)
            for k in range(3):
                print('DELAY TIME BETWEEN TASKS!', k+1 , 'SECONDS')
                time.sleep(0.9)
            pyautogui.hotkey('alt','tab')

        elif header == 'Invoice':
            # extract sku data
            pyautogui.scroll(2000)

            pyautogui.moveTo(378, 907)
            pyautogui.mouseDown(button='left')
            pyautogui.moveTo(1887, 907, duration=1)
            pyautogui.scroll(-1500)
            pyautogui.mouseUp(button='left')

            pyautogui.hotkey('ctrl', 'c')
            pyautogui.click(button='left')
            time.sleep(0.5)  # Add small delay for clipboard to update
            copied_text = pyperclip.paste()

            # print("Copied text:")
            # print(copied_text)

            # Process the text directly (no need to split/strip here)
            sku_data = extract_sku_with_context(copied_text)
            print(len(sku_data))

            change_tab('right')
            pyautogui.hotkey('ctrl','right')
            for _ in range(4):
                pyautogui.press('right')
                time.sleep(LOCAL_DELAY_TIME)
            for _ in range(len(sku_data)):
                pyautogui.press('up')
                time.sleep(LOCAL_DELAY_TIME)
            # change_tab('left')
            
            print("\nExtracted SKUs with context:")
            # change_tab('right')
            for entry in sku_data:
                print(entry[0],entry[1], entry[2], entry[3])
                temp_text = entry[0],entry[1], entry[2], entry[3]
                pyperclip.copy(temp_text)
                pyautogui.hotkey('ctrl','v')
                pyautogui.press('down')
                time.sleep(0.2)
            # change_tab('left')

            # change_tab('right')
            for _ in range(2): pyautogui.hotkey('ctrl','left')
            for _ in range(4):
                pyautogui.press('right')
                time.sleep(LOCAL_DELAY_TIME)
            change_tab('left')
            # end extract sku data

            pyautogui.hotkey('alt','tab')
            print(j+1, " invoice added")
            for k in range(3):
                print('DELAY TIME BETWEEN TASKS!', k+1 , 'SECONDS')
                time.sleep(0.9)
            pyautogui.hotkey('alt','tab')

    print('ALL DONE!!!!')

if __name__ == '__main__':
    main()