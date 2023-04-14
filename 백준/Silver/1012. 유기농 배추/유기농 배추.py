'''
1. 아이디어
 - bfs 활용 그룹 개수 구하기, 테케 존재
2. 시간복잡도
 - O(V+E)
3. 자료구조
 - 그래프 정보 int[][], 방문여부 bool []
'''
import sys
from collections import deque
input = sys.stdin.readline

# 테스트케이스
t = int(input())

# bfs
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y, x):
  q = deque()
  q.append((y, x))
  visited[y][x] = True
  while q:
    y, x = q.popleft()
    for k in range(4):
      ny, nx = y+dy[k], x+dx[k]
      if 0<=ny<n and 0<=nx<m:
        if visited[ny][nx] == False and graph[ny][nx] == 1:
          q.append((ny, nx))
          visited[ny][nx] = True
        
# main
for _ in range(t):
  m, n, k = map(int, input().split())
  graph = [[0]*m for _ in range(n)]

  # 방문정보
  visited = [[False] * m for _ in range(n)]

  # 배추정보 입력
  for _ in range(k):
    a, b = map(int, input().split())
    graph[b][a] = 1

  # 탐색
  count = 0
  for j in range(n):
    for i in range(m):
      if graph[j][i] == 1 and visited[j][i] == False:
        bfs(j, i)
        count += 1
  print(count)