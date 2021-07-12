n = int(input())

dp_list = [0 for _ in range(n+1)]

for i in range(2, n+1):
  dp_list[i] = dp_list[i-1] + 1

  if i % 3 == 0 and dp_list[i] > dp_list[i // 3] + 1 :
    dp_list[i] = dp_list[i // 3] + 1
  
  if i % 2 == 0 and dp_list[i] > dp_list[i // 2] + 1 :
    dp_list[i] = dp_list[i // 2] + 1
  
print(dp_list[n])