"""
서로소 집합을 활용한 사이클 판별
무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있다. 방향 그래프에서의 사이클 여부는 DFS를 이용하여 판단할 수 있다.

1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
    ㄱ. 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행한다.
    ㄴ. 루트 노드가 서로 같다면 사이클이 발생한 것이다.
2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다.
"""

def find_parent(parent,x):
    if parent[x] != x:
        # 경로 압축기법
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합친다
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# v : 노드의 수, e : 간선의 수
v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

# 사이클 발생여부 초기값 false
cycle = False

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 루트노드가 서로 다르다면 union 연산을 수행한다.
    else:
        union_parent(parent,a,b)

if cycle:
    print('사이클이 발생 하였습니다.')
else:
    print('사이클이 발생하지 않았습니다.')