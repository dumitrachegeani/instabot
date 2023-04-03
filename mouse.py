import time

import pyautogui

while True:
    x, y = pyautogui.position()
    print(f"Mouse position: x={x} y={y}")
    time.sleep(2)
