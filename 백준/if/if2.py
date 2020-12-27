def rangeToInput():
  condition = True
  while(condition):
    A = int(input())
    if 0 <= A <= 100:
      return A

A = rangeToInput()

if(A >= 90):
  print("A")
elif(90 > A >= 80):
  print("B")
elif(80 > A >= 70):
  print("C")
elif(70 > A >= 60):
  print("D")
else:
  print("F")