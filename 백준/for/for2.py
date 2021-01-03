def rangeToInput():
  condition = True
  while(condition):
    A,B = map(int, input().split())
    if 0 < A and B < 10:
      return A,B

count = int(input())

arr = []

for a in range(count):
  A,B = rangeToInput()
  arr.insert(a, A+B)

for a in range(count):
  print("{}".format(arr[a]))