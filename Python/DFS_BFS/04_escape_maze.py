"""
푸름이는 n x m 크기의 미로에 갇혀있다.
미로에는 여러마리 괴물이 있어 이를 피해 탈출해야 한다. 푸름이의 위치는 (1, 1)이고 미로의 출구는 (n, m)의 위치에 존재한다.
한번에 한 칸씩 이동할 수 있으며, 괴물이 있는 부분은 0 이고 괴물이 없는 부분은 1로 되어있다.
미로는 반드시 탈출할 수 있는 형태로 제시 된다. 이때 움직여야 하는 최소 칸의 갯수를 구하시오.

- 입력예시
5 6
101010
111111
000001
111111
111111

- 출력예시
10

* 이런 최단거리 문제 같은경우 BFS를 이용했을때 효과적으로 문제를 풀 수 있다.
  BFS는 시작지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색 하기 때문.
"""

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우 방향을 지정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  # 큐 초기화
  queue = deque()
  queue.append((x,y))

  # 큐가 빌때까지 계속 반복한다.
  while queue:
    x, y = queue.popleft()

    # 상하좌우로 위치를 확인한다.
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 위치를 넘어갔을 경우 pass
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      
      # 벽인 경우 pass
      if graph[nx][ny] == 0:
        continue

      # 벽이 아닐 경우 이전 값을 1씩 증가하여 기록해 준다.
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  # 가장 오른쪽 아래의 값을 출력하면 그 값이 움직이는 칸의 수이다.
  return graph[n-1][m-1]

print(bfs(0,0))
