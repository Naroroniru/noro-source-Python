
import random

userhave = int(0) 
cpuhave = int(0)
hit = 0
cpuhit = 0

def main_func():
  global userhave 
  global hit
  print("君のターン\n")
  print("更にカードを引きますか？\n")
  if hit == 0:
    print("1:引く2:引かない")
    hit = int(input())
  if hit == 1:
    list = ["hart","sperd","crober","diya"]
    mark = list[random.randint(0,3)]
    num = str(random.randint(1,10))
    ans = mark + num
    print(ans)
    userhave += int(num)
    print(userhave)
    hit = 0
  if hit == 2:
    print("パスしました。\n")
  print("-----------------------------------------------------------\n")

def cpu_func(): 
  global cpuhave
  global cpuhit
  print("CPUのターン\n")
  if cpuhave < 17:
    cpuhit = 1
  else:
    cpuhit = 2
  if cpuhit == 1:
    list = ["heart","spade","clover","dia"]
    mark = list[random.randint(0,3)]
    num = str(random.randint(1,10))
    ans = mark + num
#    print(ans)
    cpuhave += int(num)
#    print(cpuhave)
    cpuhit = 0
  if cpuhit == 2:                             
    print("パスしました。\n")
  print("-----------------------------------------------------------\n")

def jage_func():
  if userhave <= 21 and cpuhave <= 21:
    if userhave < cpuhave:
      print("君:",userhave,"CPU:",cpuhave,"で君の負け\n")
    elif userhave > cpuhave:
      print("君:",userhave,"CPU:",cpuhave,"で君の勝ち\n")
    else:
      print("君:",userhave,"CPU:",cpuhave,"で引き分け\n")
  elif userhave > 21:
    print("君:",userhave,"CPU:",cpuhave,"で君の負け\n")
  elif cpuhave > 21:
    print("君:",userhave,"CPU:",cpuhave,"で君の勝ち\n")


while hit != 2 or cpuhit != 2:
  if userhave > 21 or cpuhave > 21:
    break
  main_func()
  cpu_func()
jage_func()

