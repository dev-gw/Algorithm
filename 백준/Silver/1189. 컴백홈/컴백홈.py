'''
1. 아이디어
 - 시작점부터 dfs로 백트래킹, depth가 거리가 동일한 경우를 찾기
'''

# 입력받기
r, c, k = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

cnt = 0

visited = [[False] * c for _ in range(r)]
visited[r-1][0] = True

# 백트래킹
def dfs(y, x ,depth):
  global cnt, k
  # visited[y][x] = True
  # 종료조건
  if depth == k:
    # 집에 도착한 경우
    if y == 0 and x == c - 1:
      cnt += 1
    return
  for i in range(4):
    ny, nx = y + dy[i], x + dx[i]
    if 0<=ny<r and 0<=nx<c:
      if graph[ny][nx] != 'T' and visited[ny][nx] == False:
        visited[ny][nx] = True
        dfs(ny,nx, depth+1)
        visited[ny][nx] = False

dfs(r-1, 0, 1)
print(cnt)