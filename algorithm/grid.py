n = 1260
count = 0

arr = [500, 100, 50, 10]

for a in arr:
  count += n // a
  n = n % a

print(count)