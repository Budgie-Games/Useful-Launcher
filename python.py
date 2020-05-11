from tkinter import *
from tkinter import ttk
import os, subprocess
cwd = os.getcwd()

root = Tk()
root.geometry("145x90")
root.title("")
root.resizable(False, False)

def main():
  global cwd
  if pro.get() == "Calculator":
    path = cwd + "/calc/calculator.py"
    root.destroy()
    subprocess.call(f"{path}", shell=False)
    exit()
  elif pro.get() == "Converter":
    path = cwd + "/converter/converter.py"
    root.destroy()
    subprocess.call(f"{path}")
    exit()
  elif pro.get() == "Autoclicker":
    path = cwd + "/auto/autoclicker.py"
    root.destroy()
    subprocess.call(f"{path}", shell=False)
    exit()
  elif pro.get() == "Download Calculator":
    path = cwd + "/down/download.py"
    root.destroy()
    subprocess.call(f"{path}", shell=False)
    exit()

lab = Label(root, width=20, text="Useful Launcher v.1.P")
lab.grid()

pro = ttk.Combobox(root, width=20, values=["Calculator", "Converter", "Autoclicker", "Download Calculator"], state="readonly")
pro.grid(row=1)
pro.current(0)

validate = Button(root, width=10, text="Launch!", command=lambda: main())
validate.grid(row=2)

root.mainloop()