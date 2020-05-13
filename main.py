from tkinter import *
from tkinter import ttk
import os, subprocess
cwd = os.getcwd()

root = Tk()
root.geometry("145x90")
root.title("")
root.resizable(False, False)
bitcwd = cwd + "/budgie.ico"
root.iconbitmap(bitcwd)

def main():
  global cwd
  if pro.get() == "Calculator":
    path = cwd + "/calc/calculator.exe"
    root.destroy()
    subprocess.call(f"{path}", shell=False)
    exit()
  elif pro.get() == "Converter":
    path = cwd + "/converter/converter.exe"
    root.destroy()
    subprocess.call(f"{path}", shell=False)
    exit()
  elif pro.get() == "Autoclicker":
    path = cwd + "/auto/autoclicker.exe"
    root.destroy()
    subprocess.call(f"{path}", shell=False)
    exit()
  elif pro.get() == "Download Calculator":
    path = cwd + "/down/download.exe"
    root.destroy()
    subprocess.call(f"{path}", shell=False)
    exit()

lab = Label(root, width=20, text="Useful Launcher v.1.1")
lab.grid()

pro = ttk.Combobox(root, width=20, values=["Calculator", "Converter", "Autoclicker", "Download Calculator"], state="readonly")
pro.grid(row=1)
pro.current(0)

validate = Button(root, width=10, text="Launch!", command=lambda: main())
validate.grid(row=2)

root.mainloop()