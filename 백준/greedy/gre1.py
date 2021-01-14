N, K = map(int, input().split())
coin = []
count = 0

for i in range(N):
  coin.append(int(input()))

coin.reverse()

for i in coin:
  if i <= K:
    count += K // i
    K %= i

print(count)