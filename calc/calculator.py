from tkinter import *
import math

x10 = 0
numb = 0
numb2 = 0
arth = 0
num2 = False
equal__ = 0
dec = 0


def decimal_():
  global dec
  global num2
  global numb
  global numb2
  dec = 1
  if num2 == False:
    numb = numb / 1
    l1.config(text=numb)
  elif num2 == True:
    numb2 = numb2 / 1
    l1.config(text=numb2)


def memory():
    global mem
    if num2 == False:
            mem = numb
            mem = str(mem)
    elif num2 == True:
        if equal__ != 0:
                mem = equal__
                mem = str(mem)
        elif equal__ == 0:
                mem = numb2
                mem = str(mem)


def memprint():
    global mem
    global numb
    global numb2
    men = int(mem)
    if num2 == False:
        numb = mem
        numb = int(numb)
        l1.config(text=numb)
    elif num2 == True:
        numb2 = mem
        numb2 = int(numb2)
        l1.config(text=numb2)


def input__(num):
    global x10
    global numb
    global numb2
    global dec
    if dec == 0:
      if num2 == False:
        if x10 == 0:
            numb = num
            x10 = 1
            l1.config(text=numb)
        elif x10 == 1:
            numb = numb * 10
            numb = numb + num
            l1.config(text=numb)
      else:
        if x10 == 0:
            numb2 = num
            x10 = 1
            l1.config(text=numb2)
        elif x10 == 1:
            numb2 = numb2 * 10
            numb2 = numb2 + num
            l1.config(text=numb2)
    else:
      if dec == 1:
        if num2 == False:
          numb = numb + num / 1000000 * 100000
          numb = round(numb, 1)
          l1.config(text=numb)
          dec = dec + 1
        elif num2 == True:
          numb2 = numb2 + num / 1000000 * 100000
          numb2 = round(numb2, 1)
          l1.config(text=numb2)
          dec = dec + 1
      elif dec == 2:
        if num2 == False:
          numb = numb + num / 1000000 * 10000
          numb = round(numb, 2)
          l1.config(text=numb)
          dec = dec + 1
        elif num2 == True:
          numb2 = numb2 + num / 1000000 * 10000
          numb2 = round(numb2, 2)
          l1.config(text=numb2)
          dec = dec + 1
      elif dec == 3:
        if num2 == False:
          numb = numb + num / 1000000 * 1000
          numb = round(numb, 3)
          l1.config(text=numb)
          dec = dec + 1
        elif num2 == True:
          numb2 = numb2 + num / 1000000 * 1000
          numb2 = round(numb2, 3)
          l1.config(text=numb2)
          dec = dec + 1
      elif dec == 4:
        if num2 == False:
          numb = numb + num / 1000000 * 100
          numb = round(numb, 4)
          l1.config(text=numb)
          dec = dec + 1
        elif num2 == True:
          numb2 = numb2 + num / 1000000 * 100
          numb2 = round(numb2, 4)
          l1.config(text=numb2)
          dec = dec + 1
      elif dec == 5:
        if num2 == False:
          numb = numb + num / 1000000 * 10
          numb = round(numb, 5)
          l1.config(text=numb)
          dec = dec + 1
        elif num2 == True:
          numb2 = numb2 + num / 1000000 * 10
          numb2 = round(numb2, 5)
          l1.config(text=numb2)
          dec = dec + 1
      elif dec == 6:
        if num2 == False:
          numb = numb + num / 1000000 * 1
          numb = round(numb, 6)
          l1.config(text=numb)
          dec = dec + 1
        elif num2 == True:
          numb2 = numb2 + num / 1000000 * 1
          numb2 = round(numb2, 6)
          l1.config(text=numb2)
          dec = dec + 1

def reset():
    global numb
    global numb2
    global x10
    global num2
    global equal__
    global arth
    global dec
    arth = 0
    x10 = 0
    numb = 0
    numb2 = 0
    num2 = False
    equal__ = 0
    l1.config(text=0)
    dec = 0


def arth_(arthemic):
    global num2
    global arth
    global numb
    global numb2
    num2 = True
    global dec
    dec = 0
    if arthemic == 1:
        arth = "+"
    elif arthemic == 2:
        arth = "-"
    elif arthemic == 3:
        arth = "*"
    elif arthemic == 4:
        arth = "/"
    elif arthemic == 5:
        arth = "bin"
        num2 = False
        equal()
    elif arthemic == 6:
        if num2 == False:
            numb = math.pi
            l1.config(text=numb)
        elif num2 == True:
            numb2 = math.pi
            l1.config(text=numb2)
    elif arthemic == 7:
        if num2 == False:
            numb = math.e
            l1.config(text=numb)
        elif num2 == True:
            numb2 = math.e
            l1.config(text=numb2)
    elif arthemic == 8:
        arth = "sqrt"
        num2 = False
        equal()


def equal():
    global numb
    global numb2
    global arth
    global equal__
    equal__ = 1
    if arth == "+":
        equal__ = numb + numb2
        l1.config(text=equal__)
        numb = equal__
        numb2 = 0
    elif arth == "-":
        equal__ = numb - numb2
        l1.config(text=equal__)
        numb = equal__
        numb2 = 0
    elif arth == "*":
        equal__ = numb * numb2
        l1.config(text=equal__)
        numb = equal__
        numb2 = 0
    elif arth == "/":
        equal__ = numb / numb2
        l1.config(text=equal__)
        numb = equal__
        numb2 = 0
    elif arth == "bin":
        numb = int(numb)
        equal__ = bin(numb)
        numb = equal__
        l1.config(text=equal__)
    elif arth == "sqrt":
        numb = int(numb)
        equal__ = math.sqrt(numb)
        numb = equal__
        l1.config(text=numb)
    else:
        l1.config(text=numb)


root = Tk()
b1 = Button(root, text="1", width=1, command=lambda: input__(1))
b2 = Button(root, text="2", width=1, command=lambda: input__(2))
b3 = Button(root, text="3", width=1, command=lambda: input__(3))
b4 = Button(root, text="4", width=1, command=lambda: input__(4))
b5 = Button(root, text="5", width=1, command=lambda: input__(5))
b6 = Button(root, text="6", width=1, command=lambda: input__(6))
b7 = Button(root, text="7", width=1, command=lambda: input__(7))
b8 = Button(root, text="8", width=1, command=lambda: input__(8))
b9 = Button(root, text="9", width=1, command=lambda: input__(9))
b0 = Button(root, text="0", width=1, command=lambda: input__(0))
f1 = Frame(root, width=10, height=10)
bc = Button(root, text="C", width=1, command=lambda: reset())
f2 = Frame(root, width=10, height=10)
l1 = Label(root, text="0")
plus = Button(root, text="+", width=1, command=lambda: arth_(1))
minus = Button(root, text="-", width=1, command=lambda: arth_(2))
times = Button(root, text="x", width=1, command=lambda: arth_(3))
division = Button(root, text="/", width=1, command=lambda: arth_(4))
bequal = Button(root, text="=", width=1, command=lambda: equal())
vl1 = Label(root, text="By Knotthult")
bbin = Button(root, text="bin", command=lambda: arth_(5), width=2)
bequal.grid(row=5, column=5)
bmemory = Button(root, text="M", width=2, command=lambda: memory())
bmemoryp = Button(root, text="M+", width=2, command=lambda: memprint())
bpi = Button(root, text="Pi", width=2, command=lambda: arth_(6))
be = Button(root, text="E", width=2, command=lambda: arth_(7))
bsqrt = Button(root, text="sqrt", width=2, command=lambda: arth_(8))
bdecimal = Button(root, text=".", width=1, command=lambda: decimal_())
bdecimal.grid(row=5, column=1)
f1.grid(row=0, column=0)
f2.grid(row=5, column=4)
l1.grid(row=1, columnspan=8)
b1.grid(row=2, column=1)
b2.grid(row=2, column=2)
b3.grid(row=2, column=3)
b4.grid(row=3, column=1)
b5.grid(row=3, column=2)
b6.grid(row=3, column=3)
b7.grid(row=4, column=1)
b8.grid(row=4, column=2)
b9.grid(row=4, column=3)
b0.grid(row=5, column=2)
bc.grid(row=5, column=3)
plus.grid(row=2, column=4)
minus.grid(row=3, column=4)
times.grid(row=4, column=4)
division.grid(row=5, column=4)
vl1.grid(row=6, columnspan=5)
bbin.grid(row=4, column=6)
bmemory.grid(row=2, column=6)
bmemoryp.grid(row=3, column=6)
bpi.grid(row=2, column=7)
be.grid(row=3, column=7)
bsqrt.grid(row=4, column=7)
root.geometry("300x200")
root.title("Budgie Calculator")
root.mainloop()