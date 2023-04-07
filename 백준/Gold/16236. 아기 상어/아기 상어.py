'''
1. 아이디어
 - 조건에 맞게 bfs 탐색(최단거리 포함), 물고기 선택을 어떻게 해야할지
2. 시간복잡도
 - O(V+E) -> O(N^2) + O(4N^2)
3. 자료구조
 - 그래프 정보 int[][], 
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


# 상어 초기 정보(y좌표, x좌표,  크기)
for j in range(n):
  for i in range(n):
    if graph[j][i] == 9:
      shark_y = j
      shark_x = i

# bfs 탐색
## 상어보다 큰 숫자는 못지나감, 작은 숫자는 물고기리스트에 담기(좌표, 거리), 크기만큼 먹으면 +1
eat = 0
def bfs(y,x,size):
  # 초기화
  visited = [[False]*n for _ in range(n)]
  dist = [[0]*n for _ in range(n)]
  q = deque()
  q.append((y,x))
  visited[y][x] = True
  while q:
    y, x = q.popleft()
    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]
      if 0<=ny<n and 0<=nx<n and graph[ny][nx] <= size and visited[ny][nx] == False:
        q.append((ny, nx))
        visited[ny][nx] = True
        # 거리 탐색
        dist[ny][nx] = dist[y][x] + 1
        # 물고기 탐색
        if 0 < graph[ny][nx] < size:
          fish.append((ny, nx, dist[ny][nx]))

# main
t = 0
shark_size = 2
eat = 0
while True:
  fish = []
  bfs(shark_y, shark_x, shark_size)
  if len(fish) == 0:
    break
  # 물고기 먹기
  fish = sorted(fish, key=lambda x:(x[2],x[0],x[1]))
  # 원래있던 장소 0
  graph[shark_y][shark_x] = 0
  # 상어위치 갱신
  shark_y = fish[0][0]
  shark_x = fish[0][1]
  graph[shark_y][shark_x] = 9
  t += fish[0][2]
  eat += 1
  if eat == shark_size:
    eat = 0
    shark_size += 1

print(t)