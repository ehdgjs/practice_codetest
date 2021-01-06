A= int(input())
B= int(input())
C= int(input())

result = A*B*C
arr = []
for a in str(result):
  arr.append(a)
arr1 = [0]*10
for a in arr:
  if int(a) == 0:
    arr1[0] += 1
  elif int(a) == 1:
    arr1[1] += 1
  elif int(a) == 2:
    arr1[2] += 1
  elif int(a) == 3:
    arr1[3] += 1
  elif int(a) == 4:
    arr1[4] += 1
  elif int(a) == 5:
    arr1[5] += 1
  elif int(a) == 6:
    arr1[6] += 1
  elif int(a) == 7:
    arr1[7] += 1
  elif int(a) == 8:
    arr1[8] += 1
  elif int(a) == 9:
    arr1[9] += 1

for a in range(len(arr1)):
  print(arr1[a])
