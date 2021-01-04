import sys

def rangeToInput():
  condition = True
  while(condition):
    A = int(sys.stdin.readline().strip())
    if A <= 100000:
      return A

A = rangeToInput()
for a in range(A):
  print(a+1)