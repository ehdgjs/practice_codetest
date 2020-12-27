def rangeToInput():
  condition = True
  while(condition):
    A,B = map(int, input().split())
    if -10000 <= A <= 10000 and -10000 <= B <= 10000:
      return A,B

A,B = rangeToInput()
if A > B:
  print(">")
elif A < B:
  print("<")
elif A == B:
  print("==")