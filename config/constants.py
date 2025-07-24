"""Configuration constants for GUI automation."""

from pathlib import Path

# Base directory of the repository
BASE_DIR = Path(__file__).resolve().parents[1]

# Delay values used across actions
API_DELAY_TIME = 4
DELAY_TIME = 0.6
LOCAL_DELAY_TIME = 0.3

# Path to notification sound
SOUND_PATH = BASE_DIR / "assets" / "confirmation.wav"

# GUI coordinates (x, y)
NEW_INVOICE_BTN = (1835, 259)
CLICK_IN_BLANK = (1884, 410)
CUSTOMER_FIELD = (792, 364)
CUSTOMER_OPTION = (784, 647)
CUSTOMER_SELECT = (738, 568)
REFERENCE_FIELD = (1531, 526)
INVOICE_DATE_FIELD = (791, 607)
WAREHOUSE_FIELD = (608, 430)
WAREHOUSE_OPTION = (602, 529)
SAVE_BTN = (612, 975)
HEADER_FIELD = (441, 264)
INVALID_CLOSE_BTN = (1867, 260)
CANCEL_BTN = (764, 969)
