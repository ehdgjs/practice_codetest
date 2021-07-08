# https://www.acmicpc.net/problem/1541

# 1 + 2 - 3 + 4 - 5 + 6 으로 가정하면
# (1 + 2) - (3 + 4) - (5 + 6) 으로 계산 한 값이 가장 작은 수가 나온다
# 1. -를 split으로 잘라서 배열로 변환하면
# 2. ["1+2", "3+4", "5+6"] 이 나오고 result에 배열 첫번째 값을 더해준다
# 3. 배열 1 이후의 값들은 result에 빼준다

# 1
num_list = input().split('-')

result = 0

# 2
for i in num_list[0].split('+'):
  result += int(i)

# 3
for i in num_list[1:]:
  for j in i.split('+'):
    result -= int(j)

print(result)