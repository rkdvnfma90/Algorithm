"""
간단한 다익스트라 알고리즘
O(V ** 2) 의 시간 복잡도를 가진다. 여기서 V는 노드를 말한다.
소스코드에서 입력되는 데이터의 수가 많다는 가정하에 내장함수인 input()을 sys.std.readline()로 치환하여 사용하였다.
DFS/BFS와 마찬가지로 모든 리스트는 노드의 수 + 1 크기로 할당하여 노드의 번호를 인덱스로 하여 바로 리스트에 접근하도록 하였다.
이 방식은 그래프를 표현해야 할때 많이 사용하는 일반적인 코드 작성법이다.

이 해법의 경우 노드의 수가 5,000개 이하일 때
"""

import sys
input = sys.stdin.readline
# 무한을 의미하는 값으로써 10억을 할당한다.
INF = int(1e9)

# 노드의 갯수 n과 간선의 갯수 m을 입력받는다.
n, m = map(int, input().split())

# 시작노드번호를 입력받는다.
start = int(input()) 

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 2차원 리스트 초기화. (노드 번호를 인덱스로 하기위헤 n + 1)
graph = [[] for i in range(n + 1)]

# 해당 노드에 방문여부를 체크하는 리스트 초기화, 마찬가지로 노드 번호를 인덱스로 하기위해 n + 1
visited = [False] * (n + 1)

# 최단거리 정보를 가지고 있는 테이블을 모두 무한으로 초기화
# 이 최단거리 테이블이 의미하는 바는, ['', 0, 2, 3, 1, 2, 4] 일때 출발노드로부터 2,3,4,5,6 번 노드까지 가기위한 최단 경로가 각각 2,3,1,2,4 라는 의미다.
distance = [INF] * (n + 1)

# 모든 간선의 정보를 입력받는다.
for _ in range(m):
    # a번 노드에서 b번 노드로 가는 비용은 c라는 의미
    a, b, c = map(int, input().split())
    # b번 노드로 가는 비용을 튜플로 저장한다.
    graph[a].append((b, c))


# 방문하지 않은 노드중에서 가장 최단거리가 짧은 노드의 번호를 반환하는 함수 이 함수는 매번 단계를 반복할때 사용한다.
def get_smallest_node():
    min_value = INF
    # 가장 최단 거리가 짧은 노드 (인덱스)
    index = 0
    # 1번노드부터 시작하므로 1 ~ n 까지 반복
    for i in range(1, n + 1):
        # i 번 노드의 최단거리가 min_value 보다 작고, 아직 방문하지 않았을때
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index
    

# 다익스트라 알고리즘 함수, 매개변수로는 시작 노드를 받는다.
def dijkstra(start):
    # 시작노드의 최단거리는 자기 자신이므로 0으로 초기화 하고 방문처리 한다.
    distance[start] = 0
    visited[start] = True

    # 그래프에는 (b, c) 형태의 튜플로 되어 있으므로, 0번째 인덱스엔 도착노드가, 1번째 인덱스엔 출발노드에서 도착노드까지의 비용이 담겨 있다.
    for j in graph[start]:
        # 도착노드의 비용을 distance에 넣는다.
        distance[j[0]] = j[1]
    
    # 시작노드를 제외한 전체 n - 1 노드에 대해 반복한다.
    for _ in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리 한다.
        now = get_smallest_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드를 확인한다.
        for j in graph[now] :
            # cost 는 시작노드에서 현재노드까지의 비용 + 연결된 다른 노드까지의 비용
            cost = distance[now] + j[1]
            
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧을 경우 최단거리 테이블에 cost 를 넣는다.
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 실행
dijkstra(start)

# 모든 노드로 가기위한 최단거리 출력
for i in range(1, n + 1):
    # 도달할 수 없을 경우 
    if distance[i] == INF:
        print('도달할수없습니다.')
    # 도달할 수 있을 경우 해당 거리를 출력
    else:
        print(distance[i])