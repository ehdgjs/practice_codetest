# https://www.acmicpc.net/problem/5585

a = int(input())

b = 1000 - a

result = 0

if int(b / 500) > 0:
  result = result + int(b / 500)
  b %= 500
if int(b / 100) > 0:
  result = result + int(b / 100)
  b %= 100
if int(b / 50) > 0:
  result = result + int(b / 50)
  b %= 50
if int(b / 10) > 0:
  result = result + int(b / 10)
  b %= 10
if int(b / 5) > 0:
  result = result + int(b / 5)
  b %= 5
if int(b / 1) > 0:
  result = result + b

print(result)