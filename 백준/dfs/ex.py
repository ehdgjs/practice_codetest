def dfs(graph, v, visited):
  # visited 배열에 v를 방문 기록
  visited[v] = True
  # 방문 노드 출력
  print(v, end = ' ')
  # v번째 배열 for문
  for i in graph[v]:
    # 방문 기록이 False면 dfs 함수 실행
    if not visited[i]:
      dfs(graph, i, visited)

# 각 노드가 연결된 정보
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

# 각 노드가 방문된 정보를 표현
visited = [False]*9

# 정의된 DFS함수 호출
dfs(graph, 1, visited)