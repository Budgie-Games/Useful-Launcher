from tkinter import *
from tkinter import ttk
import os
cwd = os.getcwd()

numint = 0


def validate():
  global numint
  if value1.get() == "Hexa":
    try:
      f = numone.get()
      numint = int(f, 16)
    except TypeError:
      output.config(text="Please Insert Numbers!")
    except ValueError:
      output.config(text="Please Insert Numbers!")
  elif value1.get() == "Binary":
    try:
      f = numone.get()
      numint = int(f, 2)
    except TypeError:
      output.config(text="Please Insert Numbers!")
    except ValueError:
      output.config(text="Please Insert Numbers!")
  else:
    try:
      numint = numone.get()
      numint = int(numint)
    except TypeError:
      output.config(text="Please Insert Numbers!")
    except ValueError:
      output.config(text="Please Insert Numbers!")
  main()


def main():
  global numint
  if value2.get() == "Decimal":
    output.config(text=int(numint))
  elif value2.get() == "Binary":
    inf = bin(numint)
    inf = inf[2:]
    output.config(text=inf)
  elif value2.get() == "Hexa":
    inf = hex(numint)
    inf = inf[2:]
    output.config(text=inf)


root = Tk()

numone = StringVar()

root.geometry("164x108")
root.title("")
root.resizable(False, False)
bitcwd = cwd + "/budgie.ico"
root.iconbitmap(bitcwd)

enter = Entry(root, width=26, textvariable=numone)
enter.grid(row=0, columnspan=3)

value1 = ttk.Combobox(root, width=23, values=["Binary", "Hexa", "Decimal"], state="readonly")
value1.grid(row=1, columnspan=3)
value1.current(0)

value2 = ttk.Combobox(root, width=23, values=["Decimal", "Hexa", "Binary"], state="readonly")
value2.grid(row=3, columnspan=3)
value2.current(0)

output = Label(root, width=22, text="", borderwidth=2, relief="sunken")
output.grid(row=2, columnspan=3)

val = Button(root, width=22, text="Convert!", command=validate)
val.grid(row=4, columnspan=3)

root.mainloop()