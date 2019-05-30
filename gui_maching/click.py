import subprocess,pyautogui,time
while True:
    nextbtn = pyautogui.locateCenterOnScreen('ARROW.png')
    if nextbtn is not None:
        print("find")
        pyautogui.click(nextbtn)
        break
    time.sleep(1)
