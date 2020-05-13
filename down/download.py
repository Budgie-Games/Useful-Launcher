from tkinter import *
import os
cwd = os.getcwd()

root = Tk()

root.title("")
root.geometry("200x140")
root.resizable(False, False)
bitcwd = cwd + "/budgie.ico"
root.iconbitmap(bitcwd)

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()

var1.set("")
var2.set("0")
var3.set("")

def main():
  global var1, var2, var3, out
  size = var1.get()
  down = var2.get()
  speed = var3.get()
  try:
    size = int(size)
    down = int(down)
    speed = int(speed)
  except TypeError:
    out.config(text="Please Insert Valid Values!")
    return 0
  except ValueError:
    out.config(text="Please Insert All Values!")
    return 0
  sizee = size - down
  sizee = sizee * 1000
  speede = speed / 8
  timee1 = sizee / speede
  timem = timee1 // 60
  if timem // 60 > 0.9:
    timeh = timem // 60
    timem = timem % 60
    timeh = int(timeh)
    timem = int(timem)
    out.config(text=str(timeh) + " Hours and " + str(timem) + " Minutes!")
    return 0
  else:
    timem = int(timem)
    out.config(text=str(timem) + " Minutes!")

label1 = Label(root, text="File Size")
label2 = Label(root, text="Downloaded")
label3 = Label(root, text="Speed")
label4 = Label(root, text="GB")
label5 = Label(root, text="GB")
label6 = Label(root, text="Mbit/s")
enter1 = Entry(root, width=7, textvariable=var1)
enter2 = Entry(root, width=7, textvariable=var2)
enter3 = Entry(root, width=7, textvariable=var3)
validate = Button(root, width=7, text="Validate", command=main)
out = Label(root, text="")

label1.grid()
label2.grid(row=1)
label3.grid(row=2)
label4.grid(row=0, column=2)
label5.grid(row=1, column=2)
label6.grid(row=2, column=2)
enter1.grid(row=0, column=1)
enter2.grid(row=1, column=1)
enter3.grid(row=2, column=1)
validate.grid(row=4, column=0)
out.grid(row=5, columnspan=3)

root.mainloop()