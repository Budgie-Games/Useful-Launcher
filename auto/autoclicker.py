from tkinter import *
from tkinter import ttk
from pynput.mouse import Button, Controller
from pynput import *
import time, threading, os
import sys
sys.setrecursionlimit(10000)

root = Tk()
root.resizable(False, False)
mouse = Controller()
run = False
secdelvar = StringVar()


#Check Key
def on_press(key):
    global hot
    global run
    hotke = "z"
    try:
        key = format(key.char)
    except AttributeError:
        pass
    if key == hotke:
        if run == False:
            run = True
            clicks_()
        else:
            run = False
    else:
        pass


def clicks_():
    x = threading.Thread(target=clicks)
    x.start()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def clicks():
    global secdelvar
    global run
    ti = secdelvar.get()
    ti = float(ti)
    if run:
        if witchclick.get() == "Left":
            time.sleep(ti)
            mouse.click(Button.left, 1)
            clicks()
        elif witchclick.get() == "Middle":
            time.sleep(ti)
            mouse.click(Button.middle, 1)
            clicks()
        elif witchclick.get() == "Right":
            time.sleep(ti)
            mouse.click(Button.right, 1)
            clicks()


def listen():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


xe = threading.Thread(target=listen)
xe.start()

root.title("AC")
root.geometry("185x65")
cwd = os.getcwd()

title1 = Label(root, text="Delay")
title1.grid()

title2 = Label(root, text="s.")
title2.grid(row=0, column=2)

secdel = Entry(root, width=5, textvariable=secdelvar)
secdel.grid(row=0, column=1)

title3 = Label(root, text="Button")
title3.grid(row=1, column=0)

witchclick = ttk.Combobox(root, width=10, values=["Left", "Middle", "Right"], state="readonly")
witchclick.grid(row=1, column=1, columnspan=4)
witchclick.current(0)

title4 = Label(root, text="Hotkey Is \"z\"")
title4.grid(row=2, columnspan=2)

root.mainloop()