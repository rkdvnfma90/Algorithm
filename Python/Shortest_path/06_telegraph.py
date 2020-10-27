"""
전보문제

n개의 도시가 존재한다. 각 도시는 보내고자 하는 메세지가 있을 경우 다른 도시로 메세지를 전송할 수 있다.
하지만 x도시에서 y도시로 전보를 보내고자 한다면 x에서 y로 향하는 통로가 설치되어 있어야 한다. 예를들어 x에서 y로 향하는 통로는 있지만
y에서 x로 향하는 통로가 없다면 y는 x로 메세지를 보낼 수 없다. 또한 통로를 거쳐 메세지를 보낼 때는 일정 시간이 소요된다.
어느날 c 도시에서 최대한 많은 도시로 메세지를 보내고자 한다. 각 도시의 번호와 통로 정보가 주어졌을때,
도시 c에서 보낸 메세지를 받게되는 도시는 총 몇개이고, 도시들이 모두 메세지를 받는데 까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오.

입력조건
1. 첫째줄에 도시n, 통로m, 메세지를 보내고자 하는 도시 start 가 주어진다 (1 <= n <= 30,000, 1 <= m <= 200,000, 1 <= start <= n)
2. 둘째줄부터 m + 1 번째 줄에 걸쳐 통로에 대한 정보 x,y,z 가 주어진다.이는 도시 x에서 y로 가는 걸리는 시간 z를 의미한다. (1 <= x,y <= n, 1 <= z <= 1,000)

입력예시
3 2 1
1 2 4
1 3 2

출력예시
2 4

---
플로이드 워셜 알고리즘을 사용하기엔 n의 값이 많으므로 우선순위 큐를 이용한 다익스트라 알고리즘으로 접근해야 한다.
"""

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# n : 도시의 갯수, m : 통로의 갯수, start : 메세지를 보내고자 하는 도시 (시작점)
n, m, start = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 초기화
graph = [[] for i in range(n + 1)]

# 거리 정보를 가지고 있는 테이블 초기화
distance = [INF] * (n + 1)

# 통로(간선) 정보를 입력한다.
for _ in range(m):
  # x도시에서 y도시로 메세지가 전달되는 시간z 을 튜플로 저장한다.
  x, y, z = map(int, input().split())
  graph[x].append((y, z))


def dijkstra(start):
  q = []
  # 우선순위 큐를 사용하기 위해 최초 시작점의 거리는 0으로 세팅한다. 최단거리 테이블도 시작점은 0으로 세팅한다.
  heapq.heappush(q, (0, start))
  distance[start] = 0

  # 큐가 비어질때까지 반복
  while q:
    # 우선순위 큐에는 가장 짧은 거리의 값과 현재 노드값이 튜플로 저장되어 있기 때문에 최상단 요소를 pop한다.
    dist, now = heapq.heappop(q)

    # 만약 최단거리테이블에 저장되어 있는 현재의 값이 큐에서 꺼낸 값보다 작으면 이미 처리된 것이기 때문에 pass
    if distance[now] < dist:
      continue
    
    # 현재 노드와 인접한 노드들을 확인한다.
    for i in graph[now]:
      # cost : 현재 노드를 거쳐서 인접한 노드까지 가는 거리
      cost = dist + i[1]

      # 현재 노드를 거쳐 인접한 노드까지 가는 거리가 거리테이블에 있는 값보다 작으면 갱신한다.
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        # 갱신 후 우선순위 큐에 해당 값을 넣는다.
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 도달할 수 있는 노드의 수
count = 0
# 도달할 수 있는 노드 중에서 가장 멀리있는 노드와의 최단거리, 메세지가 동시에 발송된다고 가정할 때 가장 큰 값이 총 걸리는 시간이다.
max_distance = 0
    
for d in distance:
  if d != INF:
    count += 1
    max_distance = max(max_distance, d)

# 시작노드는 제외헤야 하므로 -1 한다.
print(count - 1, max_distance)
