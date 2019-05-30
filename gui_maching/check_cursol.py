import pyautogui

before = []
while True:
    now = pyautogui.position()
    if before != now:
        print(pyautogui.position())
    before = now
