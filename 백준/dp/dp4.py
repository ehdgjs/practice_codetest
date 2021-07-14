# https://www.acmicpc.net/problem/11726
n = int(input())

dp_list = [0 , 1, 2]

for i in range(3, n+1):
  dp_list.append(dp_list[i - 2] + dp_list[i - 1])

print(dp_list[n] % 10007)