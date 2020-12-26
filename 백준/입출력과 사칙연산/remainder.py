def rangeToInput():
  condition = True
  while(condition):
    A,B,C = map(int, input().split())
    if 2 <= A <= 10000 and 2 <= B <= 10000 and 2 <= C <= 10000:
      return A,B,C

A,B,C = rangeToInput()
print("{}".format((A+B)%C))
print("{}".format(((A%C) + (B%C))%C))
print("{}".format((A*B)%C))
print("{}".format(((A%C) * (B%C))%C))