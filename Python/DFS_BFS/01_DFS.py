def dfs(graph, v, visited):
    # 현재 노드를 방문처리 한다.
    visited[v] = True
    print(v, end= ' ')

    # 현재 노드와 연결된 노드를 재귀적으로 방문한다.
    for i in graph[v]:
        # 현재 노드가 방문하지 않은 상태라면 재귀적으로 dfs 함수를 다시 호출한다.
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 최초 방문 여부는 모두 false로 초기화 한다.
visited = [False] * 9 

dfs(graph, 1, visited)