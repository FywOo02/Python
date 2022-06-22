import time
from interval import Interval
import pyautogui

while True:
    time_now = time.strftime("%H:%M", time.localtime())
    if time_now == "06:45":
        pyautogui.moveTo(2017, 1019)
        pyautogui.click()
        break
