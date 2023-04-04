'''
1. 아이디어
 - bfs로 군집 개수 구하기, 따로 좌표입력 구현
2. 시간복잡도
 - 가능
3. 자료구조
 - 그래프정보 int[][], 방문여부 bool[][]
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
for _ in range(k):
  y, x = map(int, input().split())
  graph[y-1][x-1] = 1
visited = [[False] * m for _ in range(n)]

# bfs
def bfs(y,x):
  each = 0
  dy = [0, 1, 0, -1]
  dx = [1, 0, -1, 0]
  q = deque()
  q.append((y,x))
  while q:
    y, x = q.popleft()
    each += 1
    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]
      if 0<=ny<n and 0<=nx<m:
        if graph[ny][nx] == 1 and visited[ny][nx] == False:
          visited[ny][nx] = True
          q.append((ny, nx))
  return each
    
# logic
cnt = 0
for j in range(n):
  for i in range(m):
    if visited[j][i] == False and graph[j][i]:
      visited[j][i] = True
      cnt = max(cnt, bfs(j,i))
print(cnt)