'''
1. 아이디어 - bfs를 이용한 최단거리 도출, 목적지에 갈 수 없다면 -1
2. 시간복잡도 - O(V+E)
3. 자료구조 - 지도정보 graph[][], 방문여부 visited[][]
'''
from collections import deque

# bfs
def bfs(maps, start):
    # 크기
    n = len(maps)
    m = len(maps[0])
    # 방향
    dy = [0, 1, 0, -1]
    dx = [1, 0 ,-1, 0]
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append(start)
    visited[0][0] = True
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if maps[ny][nx] == 1 and visited[ny][nx] == False:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    maps[ny][nx] = maps[y][x] + 1
    # 최단거리
    answer = maps[n-1][m-1]
    if answer == 1:
        answer = -1
    return answer
    
def solution(maps):
    dist = bfs(maps, (0,0))
    return dist