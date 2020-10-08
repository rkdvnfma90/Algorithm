"""
n x m 크기의 얼음틀이 있다. 구멍이 뚫린 부분은 0, 막힌부분은 1로 표시 된다.
구멍이 뚫려 있는 부분끼리 상 하 좌 우로 붙어있는 경우 서로 연결되어 있는 것으로 간주한다.
얼음틀의 모양이 주어졌을때 생성되는 총 아이스크림의 갯수를 구하는 프로그램을 작성하시오.

- 입력예시
00110
00011 
11111
00000

- 출력예시
3
"""

def dfs(x, y):
    # 주어진 좌표를 벗어 났을 경우 false를 리턴한다.
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았으면 해당 노드를 방문처리 한다.
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상 하 좌 우 또한 모두 재귀적으로 호출한다.
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        # 모두 방문하였으면 true를 리턴 한다.
        return True
    # 현재 노드를 방문하였다면 false를 리턴한다.
    return False


# 얼음틀의 크기를 공백으로 구분하여 입력 받는다.
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드에 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

# 정답 출력
print(result)