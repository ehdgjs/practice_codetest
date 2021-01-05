import sys

def rangeToInputs():
  condition = True
  while(condition):
    A,B = map(int, sys.stdin.readline().strip().split())
    if 0 <= A < 10 and 0 <= B < 10 :
      return A,B

condition = True
arrA = []
arrB = []
index = 0
index1 = 0
while condition:
  A,B = rangeToInputs()
  if A == 0 and B == 0:
    break
  arrA.insert(index, A)
  arrB.insert(index, B)
  index += 1
  
while index1 != len(arrA):
  print(arrA[index1]+arrB[index1])
  index1 += 1