

N = int(input())
arr = list(map(int, input().split()))

index = 1
max = arr[0]
min = arr[0]

while index != N:
  if arr[index] > max:
    max = arr[index]
  elif arr[index] < min:
    min = arr[index]
  index += 1 
print(min, max)