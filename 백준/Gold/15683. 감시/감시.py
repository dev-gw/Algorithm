import sys
import copy

input = sys.stdin.readline

n, m = map(int, input().split())
cctv_list = []
graph = [list(map(int, input().split())) for _ in range(n)]

# cctv 정보
for j in range(n):
  for i in range(m):
    if 1 <= graph[j][i] <= 5:
      cctv_list.append((j, i, graph[j][i]))

# 방향(북동남서)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
direction = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]],
             [[0, 1], [1, 2], [2, 3], [0, 3]],
             [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]], [[0, 1, 2, 3]]]

# 감시구역
def check(graph, di, y, x):
  for i in di:
    ny = y
    nx = x
    while True:
      ny = ny + dy[i]
      nx = nx + dx[i]
      # 범위
      if nx < 0 or ny < 0 or nx >= m or ny >= n:
        break
      # 벽
      if graph[ny][nx] == 6:
        break
      elif graph[ny][nx] == 0:
        graph[ny][nx] = -1

# dfs
answer = int(1e8)
def dfs(graph, depth):
  global answer
  # 종료조건
  if depth == len(cctv_list):
    count = 0
    for i in range(n):
      count += graph[i].count(0)
    answer = min(answer, count)
    return
  y, x, di = cctv_list[depth]
  # 반복 전 그래프 저장
  copy_graph = copy.deepcopy(graph)
  for i in direction[di]:
    check(copy_graph, i, y, x)
    dfs(copy_graph, depth + 1)
    copy_graph = copy.deepcopy(graph)  # 재귀끝나면 초기화

dfs(graph, 0)
print(answer)