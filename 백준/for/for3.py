def rangeToInput():
  condition = True
  while(condition):
    A = int(input())
    if 1 <= A <= 10000:
      return A

A = rangeToInput()
result = 0
for a in range(A):
  result = result + (a+1)
print(result)