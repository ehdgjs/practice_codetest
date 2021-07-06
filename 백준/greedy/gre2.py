# https://www.acmicpc.net/problem/1931

a = int(input())

lst = []
gap = []
cur = 0
result = 0

for i in range(a):
  x,y = map(int, input().split())

  lst.append((x,y))

lst = sorted(lst, key=lambda time: time[0])

lst = sorted(lst, key=lambda time: time[1])

for i in range(len(lst)):
  if i == 0:
    cur = lst[i][1]
    result += 1
  elif lst[i][0] >= cur:
    cur = lst[i][1]
    result += 1
  
print(result)