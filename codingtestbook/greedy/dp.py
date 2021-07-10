# 92p

# 1번째 풀이
N,M,K = map(int, input().split())

lst = list(map(int, input().split()))

result = 0

# sorted에서 reverse value True로 추가해주면 역 정렬 가능
lst = sorted(lst, reverse = True)

result += lst[0] * (M - int(M / K)) + lst[1] * int(M / K)

print(result)

# 2번째 풀이
N,M,K = map(int, input().split())

lst = list(map(int, input().split()))

result = 0

# sorted에서 reverse value True로 추가해주면 역 정렬 가능
lst = sorted(lst)

first = lst[N - 1]
second = lst[N - 2]

# 예외 존재
# result += first * (M - int(M / K)) + second * int(M / K)
count = int(M / (K + 1)) * K # 반복되는 횟수를 구해서 가장 큰 값을 곱해주기
count += M % (K + 1) # 나누었을때 0으로 나누어 떨어지지 않기 때문에 값 추가

result += first * (count)
result += second * (M - count)

print(result)

# --------------------------------------------------------
# 풀이
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first1 = data[n - 1]
second1 = data[n - 2]

result = 0

while True:
  for i in range(k): # k번 반복 가능
    if m == 0:
      break
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1

print(result)