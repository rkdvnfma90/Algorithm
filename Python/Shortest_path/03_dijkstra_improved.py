"""
개선된 다익스트라 알고리즘
일반적인 다익스트라 알고리즘과 비교했을때 우선순위큐(힙)을 최단거리가 가장 짧은 노드를 찾을때 싸용하므로
get_smallest_node 함수를 작성할 필요가 없다.
"""
# 우선순위큐 (최소힙)을 사용하기 위한 heapq import
import heapq 
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 갯수 n과 간선의 갯수 m을 입력받는다.
n, m = map(int, input().split())

# 시작노드번호를 입력받는다.
start = int(input()) 

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 2차원 리스트 초기화. (노드 번호를 인덱스로 하기위헤 n + 1)
graph = [[] for i in range(n + 1)]

# 최단거리 정보를 가지고 있는 테이블을 모두 무한으로 초기화
# 이 최단거리 테이블이 의미하는 바는, ['', 0, 2, 3, 1, 2, 4] 일때 출발노드로부터 2,3,4,5,6 번 노드까지 가기위한 최단 경로가 각각 2,3,1,2,4 라는 의미다.
distance = [INF] * (n + 1)

# 모든 간선의 정보를 입력받는다.
for _ in range(m):
    # a번 노드에서 b번 노드로 가는 비용은 c라는 의미
    a, b, c = map(int, input().split())
    # b번 노드로 가는 비용을 튜플로 저장한다.
    graph[a].append((b, c))


def dijkstra(start):
    # 최단거리가 가장 짧은 노드를 선택하기위한 큐 초기화 (현재 가장 가까운 노드를 저장하기 위함)
    q = []
    # 최초 우선순위큐(최소힙)에 시작점까지의 비용과 시작점의 노드를 튜플로 삽입한다.
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # 큐가 비어 있지 않다면 계속 반복
    while q:
        # dist : 거리 , now : 현재 노드
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있다면 pass -> 큐에서 꺼낸 현재의 비용이 현재 거리테이블에 있는 비용값보다 크다면 이미 처리된 것이기 때문에 pass 한다.
        if distance[now] < dist:
            continue
        
        # 현재 노드와 인접한 다른 노드들을 확인
        for i in graph[now]:
            # cost 는 현재 노드의 거리 비용 + 현재 노드와 인접한 다른 노드까지의 비용을 합한 값을 넣는다. (cost 는 현재 노드를 거쳐 다른노드로 가는 비용)
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 distance 테이블을 cost로 갱신시켜 준다.
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # 이 값을 다시 큐에 삽입한다.
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기위한 최단거리 출력
for i in range(1, n + 1):
    # 도달할 수 없을 경우 
    if distance[i] == INF:
        print('도달할수없습니다.')
    # 도달할 수 있을 경우 해당 거리를 출력
    else:
        print(distance[i])
