def maximumInput(a):
  while True:
    arr = list(map(int, input().split()))
    if len(arr) == a:
      return arr

def avgScore(a, b):
  score = a / b * 100
  return score


N = int(input())

arr = maximumInput(N)

arr1 = []

for a in arr:
  arr1.append(avgScore(a, max(arr)))

print(sum(arr1)/N)