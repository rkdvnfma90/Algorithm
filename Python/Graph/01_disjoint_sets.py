"""
서로소 집합
공통원소가 없는 두 집합을 의미한다.
1. 합집합 연산을 확인하여 서로 연결된 두 노드 A,B를 확인한다
    ㄱ. A와 B의 루트노드 A` , B` 를 각각 찾는다.
    ㄴ. A`를 B`의 부모 노드로 설정한다 (B`가 A`를 가리킨다는 의미)
2. 모든 합집합 연산을 처리할 때 까지 1번 과정을 반복한다.

이것은 트리를 이용해 서로소 집합을 계산하는 알고리즘 이다. 실제 구현시에는
A`와 B`중에서 더 번호가 작은 원소가 부모 노드가 되도록 구현하는것이 많다.
"""

# 특정 원소의 부모 노드 찾는 함수
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을때 까지 재귀 호출 한다. (노드번호와 부모테이블의 값이 같으면 루트)
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 이 부분은 경로압축 기법을 적용하면 시간 복잡도를 개선 시킬수 있다. 경로 압축은 find 함수를 재귀적으로 호출 한 뒤에 부모테이블에 값을 갱신하는 기법이다.
def find_parent_advanced(parent, x):
    if parent[x] != x:
        parent[x] = find_parent_advanced(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치는 함수 (union)
def union_parent(parent, a, b):
    # 두 원소의 부모노드를 찾는다
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # a가 b보다 작으면 b의 부모노드를 a로 설정한다
    if a < b:
        parent[b] = a
    # 그 반대으 ㅣ경우 a의 부모노드를 b로 설정한다
    else:
        parent[a] = b

# v : 노드의 갯수와 e: 간선의 갯수 입력받기
v, e = map(int, input().split())
# 초기단계에는 가장 먼저 노드의 갯수 V 크기의 부모 테이블을 초기화 한다.
parent = [0] * (v + 1)

# 부모테이블을 초기에는 모든 노드가 부모노드로 자신을 갖고 있게 초기화 한다 (모든 노드가 루트 노드)
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 간선만큼의 수행한다.
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력, 여기에 출력된 값이 같은 것들이 집합에 속해 있는 것이다.
for i in range(1, v + 1):
    print(find_parent(parent, i), end = ' ')
print()

# 부모 테이블 내용 출력
print('부모테이블 : ', end = ' ')
for i in range(1, v + 1):
    print(parent[i], end = ' ')