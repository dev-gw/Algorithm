'''
1. 아이디어 - 쿼리마다 bfs 실행
2. 시간복잡도 - O(V+E)
3. 자료구조 - 그래프정보 int[][], 방문여부 bool[][]
'''
from collections import deque

# bfs
def bfs(graph, y,x, max_virus, rows, columns):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    visited = [[False] * columns for _ in range(rows)]
    q = deque()
    q.append((y,x))
    visited[y][x] = True
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x+dx[k]
            # 증식 조건 확인
            if 0<=ny<rows and 0<=nx<columns:
                if visited[ny][nx] == False and graph[ny][nx] < max_virus:
                    graph[ny][nx] += 1
                    visited[ny][nx] = True
                if visited[ny][nx] == False and graph[ny][nx] == max_virus:
                    q.append((ny, nx))
                    visited[ny][nx] = True
    return graph

# main
def solution(rows, columns, max_virus, queries):
    graph = [[0] * columns for _ in range(rows)]
    for query in queries:
        y, x = query[0]-1, query[1]-1
        # 최대 미만
        if graph[y][x] < max_virus:
            graph[y][x] += 1
        # 증식
        elif graph[y][x] == max_virus:
            graph = bfs(graph, y, x, max_virus, rows, columns)
        
    answer = graph
    return answer
