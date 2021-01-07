N = int(input())

arr = []
arr1 = []
arr2 = []
for a in range(N):
  arr.append(input())

for a in range(N):
  arr3 = []
  score = 0
  count = 0
  for b in arr[a]:
    arr3.append(b)
  for c in arr3:
    if c == 'O':
      count += 1
      score += count
    elif c == 'X':
      count = 0
  print(score)


