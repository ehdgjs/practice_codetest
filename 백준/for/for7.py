#  for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.
# map(int,sys.stdin.readline().strip().split())
import sys

def rangeToInput():
  condition = True
  while(condition):
    A = int(sys.stdin.readline().strip())
    if A <= 1000000:
      return A

def rangeToInputs():
  condition = True
  while(condition):
    A,B = map(int, sys.stdin.readline().strip().split())
    if A <= 1000000:
      return A,B

index = rangeToInput()
arr = []

for a in range(index):
  A,B = rangeToInputs()
  arr.insert(a, A+B)

for a in range(index):
  print("Case #{0}: {1}".format(a+1,arr[a]))