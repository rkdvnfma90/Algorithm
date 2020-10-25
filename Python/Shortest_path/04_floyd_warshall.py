"""
플로이드 워셜 알고리즘
다이나믹 프로그래밍의 특징을 가지고 있다. 
전체 시간복잡도는 O(N ** 3) 이다.

기본 개념 : a에서 b로 갈때의 거리와, a에서 k를 거쳐 b로 갈때의 거리를 비교하여 더 작은값을 a에서 b로 갈때의 거리로 설정한다.
점화식 : a -> b = min( a -> b, a -> k + k -> b ) 
"""

# 무한을 의미하는 값으로 10억을 설정한다.
INF = int(1e9)

# 노드의 갯수 및 간선의 갯수를 입력 받는다
n = int(input())
m = int(input())

# 2차원 리스트(그래프)를 만들고 모든 값을 무한으로 초기화 한다. (노드 번호를 인덱스로 편하게 사용하기 위해 n + 1)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0 으로 초기화 한다.
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화 한다.
for _ in range(m):
    # a에서 b로 가는 비용은 c 라고 설정한다
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라서 플로이드 워셜 알고리즘 수행
# k : 거쳐가는 노드, a : 출발노드, b : 도착노드
for k in range(1, n + 1): # 
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


# 수행된 결과를 출력
for a in range(1 , n + 1):
    for b in range(1, n +1):
        if graph[a][b] == INF:
            print("도달할수없습니다.", end = ' ')
        else:
            print(graph[a][b], end = ' ')
    print()
