import os
t = None
inf = None
s = None

def main():
  global t, inf, s
  os.system("cls" if os.name == "nt" else "clear")
  print('Type "exit" to exit!')
  t = input("Input type: 1:Bin | 2:Oct | 3:Hex | 4:Decimal > ")
  os.system("cls" if os.name == "nt" else "clear")
  
  if t == "exit":
    os.system("python main.py")
    exit()

  inf = input(" > ")
  os.system("cls" if os.name == "nt" else "clear")
  
  if t == "3":
    t = t.upper()
    try:
      s = int(inf, 16)
    except TypeError:
      invalid()
    ende()

  elif t == "1":
    try:
      s = int(inf, 2)
    except TypeError:
      invalid()
    ende()

  elif t == "2":
    try:
      s = int(inf, 8)
    except TypeError:
      invalid()
    ende()
  
  else:
    try:
      s = int(inf)
    except TypeError:
      invalid()
    except ValueError:
      invalid()
    ende()


def ende():
  global t, inf, s
  os.system("cls" if os.name == "nt" else "clear")
  t = input("Output type: 1:Bin | 2:Oct | 3:Hex | 4:Decimal > ")
  
  if t == "3":
    he = hex(s)
    he = he[2:]

  elif t == "1":
    he = bin(s)
    he = he[2:]
  
  elif t == "2":
    he = oct(s)
    he = he[2:]

  else:
    he = s

  os.system("cls" if os.name == "nt" else "clear")
  input(he)
  main()


def invalid():
  os.system("cls" if os.name == "nt" else "clear")
  input("Invalid Input!")
  os.system("cls" if os.name == "nt" else "clear")
  main()


main()
