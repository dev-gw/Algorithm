'''
1. 아이디어
 - 구현, 스텝별로, 칸별로 나무가 중복되는것 고려 -> 3차원배열
2. 시간복잡도
3. 자료구조
 - 땅 정보 그래프 int [][](양분정보), 나무정보 튜플 int[][][] -> 나무개수만큼 나이가 추가된다.
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
s2d2 = [list(map(int, input().split())) for _ in range(n)]
tree = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
  x, y, z = map(int, input().split())
  tree[x-1][y-1].append(z)

# 초기 양분(a는 줄양분, graph는 현재양분)
graph = [[5] * n for _ in range(n)]

def season():
  global tree, graph
  dy = [-1, -1, -1, 0, 0, 1, 1, 1]
  dx = [-1, 0, 1, -1, 1, -1, 0, 1]
  # 봄, 여름(성장, 죽음)

  for i in range(n):
    for j in range(n):
      t_len = len(tree[i][j])
      for k in range(t_len):
        # 양분섭취
        if graph[i][j] >= tree[i][j][k]:
          graph[i][j] -= tree[i][j][k]
          tree[i][j][k] += 1
        else:
          # 양분이 부족한 이후는 다 죽는 나무
          for _ in range(k,t_len):
            graph[i][j] += tree[i][j].pop() // 2
          break
        
  # 가을(번식)
  for i in range(n):
    for j in range(n):
      for each in tree[i][j]:
        if each % 5 == 0:
          for k in range(8):
            ny = j + dy[k]
            nx = i + dx[k]
            if 0<=ny<n and 0<=nx<n:
              tree[nx][ny].appendleft(1)
      # 겨울
      graph[i][j] += s2d2[i][j]

# main
for i in range(k):
  season()

result = 0
for i in range(n):
  for j in range(n):
    result += len(tree[i][j])

print(result)