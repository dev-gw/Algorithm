'''
1. 아이디어
 - BFS 실행될때마다 그림 1개 
 - 방문여부 중요
 - BFS가 4방향 확인
2. 시간복잡도 - O(V+E) , V : NM, E < 4NM
3. 자료구조
 - 그래프 정보 int[][]
 - 방문여부 bool[][]
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt = 0
result = 0

# BFS
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def bfs(y,x):
  rs = 1
  q = deque()
  q.append((y, x))
  while q:
    y, x = q.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if 0<=ny<n and 0<=nx<m:
        if graph[ny][nx] == 1 and visited[ny][nx] == False:
          q.append((ny, nx))
          visited[ny][nx] = True
          rs += 1
  return rs
    
# logic
for j in range(n):
  for i in range(m):
    if graph[j][i] == 1 and visited[j][i] == False:
      cnt += 1
      visited[j][i] = True
      result = max(result, bfs(j, i))

print(cnt)
print(result)
