N = int(input())

data = list(map(int,input().split()))
data.sort()

result = 0
count = 0
for a in data:
  count += 1
  if a == count:
    result += 1
    count = 0
    
print(result)
