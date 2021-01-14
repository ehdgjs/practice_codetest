N = int(input())
x, y = 1, 1
datas = input().split()

# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
types = ['L', 'R', 'U', 'D']

for data in datas:
  for i in range(len(types)):
    if data == types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or ny < 1 or nx > N or nx > N:
    continue
  x, y = nx, ny
  
print(x, y)