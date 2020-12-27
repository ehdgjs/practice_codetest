def rangeToInput():
  condition = True
  while(condition):
    A = int(input())
    if (-1000 <= A <= 1000 and A != 0):
      return A

x = rangeToInput()
y = rangeToInput()
if x > 0 and y > 0:
  print("1")
elif x < 0 and y > 0:
  print("2")
elif x < 0 and y < 0:
  print("3")
else:
  print("4")