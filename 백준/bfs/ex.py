from collections import deque

def bfs(graph, start, visited):
  # start로 시작하는 큐 생성
  queue = deque([start])
  # 방문 처리
  visited[start] = True
  # 큐가 empty 될때까지 반복
  while queue:
    # 큐에서 출력된 원소 v에 저장
    v = queue.popleft()
    # v 출력
    print(v, end=' ')
    # 출력된 원소 인접 원소 for문
    for i in graph[v]:
      # 인접 원소 중 방문하지 않은 원소 큐에 저장, 방문
      if not visited[i]:
        queue.append(i)
        visited[i] = True

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

# 정의된 BFS함수 호출
bfs(graph, 1, visited)