'''
1. 아이디어 -> 구현, 4방향 탐색, 후진할 경우 그 칸은 청소가 되어있음
              0 = 청소x, 1 = 벽, 2 = 청소 o
2. 시간복잡도 -> O(NM), 구현가능
3. 자료구조 -> int[][], d, cnt
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
cnt = 0

# simulation
while True:
  if array[y][x] == 0:
    array[y][x] = 2
    cnt += 1
  temp = False
  for i in range(1,5):
    ny = y + dy[d-i]
    nx = x + dx[d-i]
    if 0<=ny<N and 0<=nx<M:
      if array[ny][nx] == 0:
        d = (d-i+4)%4
        y = ny
        x = nx
        temp = True
        break
  if temp == False:
    ny = y + dy[d-2]
    nx = x + dx[d-2]
    if 0<=ny<N and 0<=nx<M:
      if array[ny][nx] == 1:
        break
      else:
        y = ny
        x = nx
    else:
      break

print(cnt)