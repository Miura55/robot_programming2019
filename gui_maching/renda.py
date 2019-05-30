from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener
import threading, time


def mouseclick(e):
    while not e.isSet():
        Controller().click(Button.left)
        time.sleep(0.1)

def on_press(key):
    global e
    if key == Key.f2:
        if e.isSet():
            e.clear()
        else:
            e.set()
    if key == Key.esc:
        return False

e = threading.Event()
t = threading.Thread(target=mouseclick, args=(e,))
t.setDaemon(True)
t.start()

with Listener(on_press=on_press) as listener:
    listener.join()
