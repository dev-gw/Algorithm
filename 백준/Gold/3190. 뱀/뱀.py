'''
1. 아이디어
 - 조건에 맞게 구현, 방향전환 생각
2. 시간복잡도
 - 가능
3. 자료구조
 - 그래프(지도) 정보 int [][] -> 뱀, 사과 표현, 꼬리 변수
'''
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
k = int(input())
# 지도 정보 (1-뱀, 2-사과)
graph = [[0] * n for _ in range(n)]
# 사과 입력
for _ in range(k):
  a, b = map(int, input().split())
  graph[a-1][b-1] = 2
# 변환정보
l = int(input())
rotate = defaultdict(int)
for _ in range(l):
  c, d = input().split()
  rotate[int(c)] = d
  
t = 0
y = x = 0
direction = 0
tail = deque()
tail.append((y,x))
graph[y][x] = 1
# 동남서북
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# main
while True:
  t += 1
  # 이동
  ny = y + dy[direction]
  nx = x + dx[direction]
  if 0 > nx or nx >= n or 0 > ny or ny >= n:
    break
  if graph[ny][nx] == 2:
    graph[ny][nx] = 1
    y = ny
    x = nx
    tail.append((y,x))
  # 사과가 없다면 꼬리 업데이트
  elif graph[ny][nx] == 0:
    graph[ny][nx] = 1
    y = ny
    x = nx
    tail.append((y,x))
    tail_y, tail_x = tail.popleft()
    graph[tail_y][tail_x] = 0
  else:
    break
  # 방향전환
  if t in rotate.keys():
    if rotate[t] == 'L':
      direction = (direction-1+4)%4
    elif rotate[t] == 'D':
      direction = (direction+1+4)%4

print(t)