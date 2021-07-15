import time
start=time.time()
n = int(input())

lst = []
color = 0
result = 0

for _ in range(n):
  lst.append(list(map(int, input().split())))

color = lst[0].index(min(lst[0]))

result += min(lst[0])

for i in range(1, n):
  k = lst[i]
  k.pop(color)

  result += min(k)
  color = lst[i].index(min(k))

print(result)
print(time.time() - start)
# 시간초과