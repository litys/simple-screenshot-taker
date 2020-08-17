import pyautogui # screenshot
from datetime import datetime # date
import time # Sleep

doLoop = True
interval = 60 # How long wait untill take another screenshot (sec)
counter = 60 # How many screenShots (working time = interval * counter)

while doLoop:
    time.sleep(interval)

    now = datetime.now()

    current_time = now.strftime("%H-%M-%S")

    pic = pyautogui.screenshot()

    pic.save(current_time+'.png')

    counter = counter - 1
    if counter <= 0:
        doLoop = False