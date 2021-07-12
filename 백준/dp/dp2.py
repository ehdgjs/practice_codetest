# https://www.acmicpc.net/problem/9095

n = int(input())

for _ in range(n):
  m = int(input())
  dp_list = [0, 1, 2, 4]

  for i in range(4, m+1):
    dp_list.append(dp_list[i-3] + dp_list[i-2] + dp_list[i-1])

  print(dp_list[m])