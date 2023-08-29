def lst_nb1(lst):
  lst_1 =[]
  for i in lst:
    j = i.split()
    lst_1.append(j[0])
  return lst_1

def lst_nb2(lst):
  lst_2 =[]
  for i in lst:
    j = i.split()
    lst_2.append(j[2])
  return lst_2

def lst_oper(lst):
  lst_o =[]
  for i in lst:
    j = i.split()
    lst_o.append(j[1])
  return lst_o

def total(lst1, lst0, lst2):
  lst_total = []
  for k in range(len(lst1)):
    if lst0[k] == "+":
      lst_total.append(str(int(lst1[k]) + int(lst2[k])))
    else: 
      lst_total.append(str(int(lst1[k]) - int(lst2[k])))
  return lst_total

def error_1(l):
  if l >= 5:
    print("Error: Too many problems.")
    return True
  else: return False

def error_2(lst0):
  for i in lst0:
    if i == "*" or i == "/":
      print("Error: Operator must be '+' or '-'.")
      return True
  return False 

def error_3(lst1, lst2):
  for i in lst1:
    try:
      int(i)
    except:
      print("Error: Numbers must only contain digits.")
      return True
  for j in lst2:
    try:
      int(j)
    except:
      print("Error: Numbers must only contain digits.")
      return True
  return False

def error_4(lst1, lst2):
  for i in lst1:
    if int(i) > 9999:
      print("Error: Numbers cannot be more than four digits.")
      return True
  for j in lst2:
    if int(j) > 9999:
      print("Error: Numbers cannot be more than four digits.")
      return True
  return False

def prt(lst1, lst0, lst2, lstt):
  l = len(lst1)
  lst_tick = []
  for i in range(l):
    if len(lst1[i]) >= len(lst2[i]):
      r = len(lst1[i]) + 2
      lst_tick.append("-"*r + " "*4)
      lst1[i] = " "*2 + lst1[i] + " "*4
      lst2[i] = lst0[i] + " "*(r-len(lst2[i])-1) + lst2[i] + " "*4
      lstt[i] = " "*(r-len(lstt[i])) + lstt[i] + " "*4
    else: 
      r = len(lst2[i]) + 2
      lst_tick.append("-"*r + " "*4)
      lst1[i] = " "*(r-len(lst1[i])) + lst1[i] + " "*4
      lst2[i] = lst0[i] + " " + lst2[i] + " "*4
      lstt[i] = " "*(r-len(lstt[i])) + lstt[i] + " "*4
  for i in lst1:
    print(i, end="")
  print()
  for i in lst2:
    print(i, end="")
  print()
  for i in lst_tick:
    print(i, end="")
  print()
  for i in lstt:
    print(i, end="")

def arithmetic_arranger(lst, finish):
  lst_1 = lst_nb1(lst)
  lst_2 = lst_nb2(lst)
  lst_o = lst_oper(lst)
  if error_3(lst_1, lst_2): exit()
  if error_1(len(lst_1)): exit()
  if error_2(lst_o): exit()
  if error_4(lst_1, lst_2): exit()
  lst_total = total(lst_1, lst_o ,lst_2)
  prt(lst_1, lst_o, lst_2, lst_total)
