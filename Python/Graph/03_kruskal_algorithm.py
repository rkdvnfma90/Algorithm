"""
크루스칼 알고리즘 (서로소 집합 알고리즘을 사용)
크루스칼 알고리즘을 사용하면 가장 적은 비용으로 모든 노드를 연결할 수 있다. (그리디 알고리즘으로 분류됨)
먼저 모든 간선에 대하여 정렬을 수행한 뒤에 가장 거리가 짧은 간선부터 집합에 포함 시키면 된다. 이때 사이클을 발생시킬 수 있는 간선의 경우 집합에 포함시키지 않는다.

1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
    ㄱ. 사이클이 발생하지 않으면 최소 신장트리에 포함시킨다.
    ㄴ. 사이클이 발생하는 경우 최소 신장트리에 포함시키지 않는다.
3. 모든 간선에 대하여 2번의 과정을 반복한다.
"""

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트노드가 아니라면 루트 노드를 찾을 때 까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    # 두 원소의 루트 노드를 구한다.
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 수와 간선(union 연산)의 수를 입력받는다.
v, e = map(int, input().split())
# 부모 테이블을 초기화 한다
parent = [0] * (v + 1)

# 부모 노드를 자기의 노드 번호로 초기화 한다.
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수를 선언한다.
edges = []
result = 0

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    # a노드와 연결되어 있는 b노드의 비용 cost
    a, b, cost = map(int, input().split())

    # 비용 순으로 정렬하기 위하여 튜플의 첫번째 원소를 cost로 넣는다 (튜플은 정렬할때 첫번째 값을 기준으로 정렬함)
    edges.append((cost, a, b))

# 간선을 비용 순으로 정렬한다
edges.sort()

# 간선을 하나씩 확인한다
for edge in edges:
    cost, a, b = edge

    # 사이클이 발생하지 않을 경우에만 집합에 포함 시킨다. 사이클이 발생하지 않는 경우는 부모의 노드가 다를때 이다.
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
