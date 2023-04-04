'''
1. 아이디어
 - bfs 탐색을 통한 최단거리(격자활용)
2. 시간복잡도
3. 자료구조
 - 그래프정보 int[][]
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# bfs
def bfs(y,x):
  dy = [0, 1, 0, -1]
  dx = [1, 0, -1, 0]
  q = deque()
  q.append((y,x))
  while q:
    y, x = q.popleft()
    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]
      if 0<=ny<n and 0<=nx<m:
        if visited[ny][nx] == False and graph[ny][nx] == 1:
          visited[ny][nx] = True
          graph[ny][nx] = graph[y][x] + 1
          q.append((ny, nx))
bfs(0,0)
print(graph[n-1][m-1])