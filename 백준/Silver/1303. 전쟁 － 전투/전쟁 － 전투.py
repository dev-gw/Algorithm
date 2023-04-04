'''
1. 아이디어
 - BFS 그래프탐색, 내부 개수^2 더해주기, 소속에 따른 조건분기
2. 시간복잡도
 - O(V+E), 가능
3. 자료구조
 - 그래프 char[][], 방문여부 bool[][], 위력 변수 2개
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

# bfs
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def bfs(y, x):
  cnt = 1
  q = deque()
  q.append((y,x))
  while q:
    y, x = q.popleft()
    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]
      if 0<=ny<m and 0<=nx<n:
        if visited[ny][nx] == False and graph[y][x] == graph[ny][nx]:
          visited[ny][nx] = True
          q.append((ny, nx))
          cnt += 1
  return cnt

# logic
white = 0
blue = 0
for i in range(m):
  for j in range(n):
    if visited[i][j] == False:
      if graph[i][j] == 'W':
        visited[i][j] = True
        white += bfs(i,j) ** 2
      else:
        visited[i][j] = True
        blue += bfs(i,j) ** 2

print(white, end=' ')
print(blue)