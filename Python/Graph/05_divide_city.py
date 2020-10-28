"""
도시분할 계획
마을은 n개의 집과 m개의 길로 이루어져 있다. 길은 길마다 유지하는데 드는 유지비가 있다.
해당 마을을 2개의 분리된 마을로 분할할 계획을 세우고 있다.
마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야 한다.
즉 두 집 사이에 경로가 항상 존재해야 한다.

입력조건
1. 첫째줄에 집의개수 n , 길의개수 m 이 주어진다. (2 <= n <= 100,000 , 1 <= m <= 1,000,000)
2. 그 다음줄 부터 m줄에 걸쳐 길의 정보가 a,b,c 3개의 정수로 공백으로 주어지는데 
   a번집에서 b번집으로 연결되어 있는 길의 유지비가 c 라는 의미이다. (1 <= c <= 1,000)

출력조건
1. 길을 없애고 남은 유지비의 합의 최솟값을 출력한다.

풀이
핵심 아이디어는 전체의 그래프에서 2개의 최소신장트리를 만들어야 한다. 
크루스칼 알고리즘을 통해 최소 신장트리를 만들고, 간선 중에서 가장 비용이 큰 간선을 제거하는 것이다.
"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드수와 간선의 수를 입력 받는다.
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 간선리스트와, 비용의 합이 저장될 result 변수 초기화
edges = []
result = 0

# 부모 테이블은 최초 자신의 노드 값으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 간선의 정보 입력받기
for _ in range(e):
    # a에서 b로 가는 비용 cost
    a, b, cost = map(int, input().split())

    # 비용순으로 정렬하기위해 튜플로 담는다
    edges.append((cost, a, b))

# 크루스칼 알고리즘을 사용하기위해 비용으로 정렬한다.
edges.sort()
# 최소신장 트리에 존재하는 간선중 가장 큰 값
last = 0

# 간선을 하나씩 확인한다.
for edge in edges:
    cost, a, b = edge

    # 사이클이 발생하지 않을때 집합에 포함시킨다
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        # 이때 해당되는 비용을 result에 저장한다.
        result += cost
        # 간선은 비용이 오름차순으로 되어 있으므로 결국 last에는 가장 큰값이 들어간다
        last = cost

# 결과값에서 가장 큰 간선의 값을 뺀다.
print(result - last)