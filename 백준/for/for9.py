import sys

def rangeToInput():
  condition = True
  while(condition):
    A = int(sys.stdin.readline().strip())
    if 1 <= A <= 100:
      return A

A = rangeToInput()
for a in range(A):
  for c in range(A-(a+1)):
    print(" ", end="")
  for b in range(a+1):
    print("*", end="")
  print("")
  