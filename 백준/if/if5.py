def rangeToInput():
  condition = True
  while(condition):
    A,B = map(int, input().split())
    if 0 <= A <= 23 and 0 <= B <= 59:
      return A,B

H, M = rangeToInput()

if M < 45:
  if H == 0:
    print("{0} {1}".format(23, 60-(45-M)))
  else:
    print("{0} {1}".format(H-1, 60-(45-M)))
else:
  if M > 45:
    print("{0} {1}".format(H, M-45))
  else:
    print("{0} {1}".format(H, 45-M))