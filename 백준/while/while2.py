import sys

def rangeToInputs():
  condition = True
  while(condition):
    A,B = map(int, input().split())
    if 0 <= A < 10 and 0 < B < 10 :
      return A,B

index = 0
index1 = 0
arrA = []
arrB = []

try:
  while True:
    A, B = rangeToInputs()
    arrA.insert(index, A)
    arrB.insert(index, B)
    index += 1
except:
  while index1 != len(arrA):
    print(arrA[index1]+arrB[index1])
    index1+=1