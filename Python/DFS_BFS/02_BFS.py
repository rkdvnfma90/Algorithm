from collections import deque

def bfs(graph, start, visited):
  # 큐 구현을 위해 덱 라이브러리 사용
  queue = deque([start])

  # 현재 노드를 방문 처리
  visited[start] = True

  # 큐가 빌때까지 반복
  while queue:
      # 큐에서 하나의 원소를 pop 한다.
      v = queue.popleft()
      print(v, end = ' ')
      # 현재 pop 한 원소와 연결되고, 아직 방문하지 않은 원소들을 큐에 삽입한다.
      for i in graph[v]:
          if not visited[i]:
              queue.append(i)
              visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)