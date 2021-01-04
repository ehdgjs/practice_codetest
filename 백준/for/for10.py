import sys

def rangeToInput():
  condition = True
  while(condition):
    A,B = map(int, sys.stdin.readline().strip().split())
    if 1 <= A <= 10000 and 1 <= B <= 10000:
      return A,B
    

A,B = rangeToInput()
num_list = list(map(int, sys.stdin.readline().strip().split()))

for a in num_list:
  if a < B:
    print(a, end=" ")