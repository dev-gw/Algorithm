'''
1. 아이디어
 - 4방향 움직임에 따른 함수 구현(주사위 모든 면 업데이트), 4방향 움직임 좌표 설정
2. 시간복잡도
 - O(N)
3. 자료구조
 - 주사위 면 정보 int[], 그래프 정보 int[][]
'''
import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
result = []
# 주사위 면 정보(전개도와 동일)
dice = [0] * 7

# 동쪽 움직임
def east(new):
  top = dice[1]
  dice[1], dice[4], dice[6], dice[3] = dice[4], dice[6], dice[3], top
  print(dice[1])
  if new == 0:
    return dice[6]
  else:
    dice[6] = new
    return 0

# 서쪽 움직임
def west(new):
  # 현재 윗면
  top = dice[1]
  dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], top
  print(dice[1])
  if new == 0:
    return dice[6]
  else:
    dice[6] = new
    return 0

# 북쪽 움직임
def north(new):
  top = dice[1]
  dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], top
  print(dice[1])
  if new == 0:
    return dice[6]
  else:
    dice[6] = new
    return 0

# 남쪽 움직임
def south(new):
  top = dice[1]
  dice[1], dice[2], dice[6], dice[5] = dice[2], dice[6], dice[5], top
  print(dice[1])
  if new == 0:
    return dice[6]
  else:
    dice[6] = new
    return 0

# main
def move(y, x):
  for each in order:
    # 동쪽
    if each == 1:
      ny = y
      nx = x + 1
      if 0<=ny<n and 0<=nx<m:
        fig = east(graph[ny][nx])
        graph[ny][nx] = fig
        y = ny
        x = nx
      else:
        continue
    # 서쪽
    elif each == 2:
      ny = y
      nx = x - 1
      if 0<=ny<n and 0<=nx<m:
        fig = west(graph[ny][nx])
        graph[ny][nx] = fig
        y = ny
        x = nx
      else:
        continue
    # 북쪽
    elif each == 3:
      ny = y - 1
      nx = x
      if 0<=ny<n and 0<=nx<m:
        fig = north(graph[ny][nx])
        graph[ny][nx] = fig
        y = ny
        x = nx
      else:
        continue
    # 남쪽
    elif each == 4:
      ny = y + 1
      nx = x
      if 0<=ny<n and 0<=nx<m:
        fig = south(graph[ny][nx])
        graph[ny][nx] = fig
        y = ny
        x = nx
      else:
        continue
      
move(x, y)