
k = input()

#print(k)

ans = ""

print("----------------------------------------------------------------------")
for x in k:
#  print(ord(x))
  
  if ord("A") <= ord(x) and ord(x) <= ord("M") or ord("a") <= ord(x) and ord(x) <= ord("m"): 
    ans += chr(ord(x) + 13) 

  elif ord("N") <= ord(x) and ord(x) <= ord("Z") or ord("n") <= ord(x) and ord(x) <= ord("z"):
  
    ans += chr(ord(x) - 13)

#  elif ord("a") <= ord(x) and ord(x) <= ord("m"):
#    ans += chr(ord(x) + 13)

#  elif ord("n") <= ord(x) and ord(x) <= ord("z"):
#    ans += chr(ord(x) - 13) 

  else :
    ans += x
print(ans)

