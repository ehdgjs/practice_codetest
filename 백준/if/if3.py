def rangeToInput():
  condition = True
  while(condition):
    A = int(input())
    if 1 <= A <= 4000:
      return A

A = rangeToInput()

if (A % 4 == 0 and A % 100 != 0) or A % 400 == 0:
  print("1")
else:
  print("0")