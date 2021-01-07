arr = []
arr1 = []
for a in range(10):
  A = int(input())
  arr.insert(a, A)

for a in arr:
  arr1.append(a%42)

#집합은 중복을 생략해준다.
print(len(set(arr1)))