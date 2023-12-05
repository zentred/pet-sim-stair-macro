import time, threading
from pynput import keyboard
from pynput.keyboard import Key

exitKey = "-"
exitMacro = False

def on_press(key):
    global exitMacro
    try:
        if key.char == exitKey:
            exitMacro = True
            keyboard.release('d')
    except:
        if key == exitKey:
            exitMacro = True
            keyboard.release('d')

listener = keyboard.Listener(
    on_press=on_press)
listener.start()

time.sleep(3)
keyboard = keyboard.Controller()
keyboard.press('d')

while not exitMacro:
    keyboard.press(Key.left)
    time.sleep(0.13)
    keyboard.release(Key.left)
    time.sleep(0.15)