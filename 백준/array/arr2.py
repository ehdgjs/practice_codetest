arr = []
for a in range(9):
  A = int(input())
  arr.insert(a, A)

max = arr[0]
index = 0

for a in range(len(arr)):
  if arr[a] > max:
    max = arr[a]
    index = a
print(max)
print(index+1)