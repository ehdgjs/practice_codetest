# https://www.acmicpc.net/problem/1003

n = int(input())

for _ in range(n):
  m = int(input())

  dp0_list = [1, 0]
  dp1_list = [0, 1]

  for i in range(2,m+1):
    dp0_list.append(dp0_list[i-2] + dp0_list[i-1])
    dp1_list.append(dp1_list[i-2] + dp1_list[i-1])

  print(dp0_list[m], dp1_list[m])

