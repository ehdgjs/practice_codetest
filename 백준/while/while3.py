import sys

def rangeToInputs():
  condition = True
  while(condition):
    A = int(sys.stdin.readline().strip())
    if 0 <= A < 100 :
      return A
A = rangeToInputs()
index = 1
B = A
while True:
  a = int(A/10)
  b = A%10
  A = int(str(b)+str((a+b)%10))
  index += 1
  if B == A:
    index -= 1
    break
print(index)