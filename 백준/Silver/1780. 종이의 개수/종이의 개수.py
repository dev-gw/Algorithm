'''
1. 아이디어
 - 기존 재귀문제랑 비슷 (종이 9등분), 먼저 조건 확인 후 만족안하면 재귀9번 실행

2. 시간복잡도
 - O(9N^2)

3. 자료구조
 - 그래프정보 int[][]
'''

import sys
input = sys.stdin.readline

# 개수 입력
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# -1, 0, 1 개수
count_1 = 0
count_2 = 0
count_3 = 0

# 같은 숫자로 이루어져 있는지 확이
def check(y, x, size):
  init = graph[y][x]
  for j in range(y, y+size):
    for i in range(x, x+size):
      if init != graph[j][i]:
        return False
  return True

# 재귀 (시작점, 사이즈 입력)
def reculsive(y, x, size):
  global count_1, count_2, count_3
  # 같은 숫자로 이루어져 있는 경우
  if check(y, x, size):
    if graph[y][x] == -1:
      count_1 += 1
    elif graph[y][x] == 0:
      count_2 += 1
    else:
      count_3 += 1
    return
    
  # 같은 숫자가 아닌경우 다시 탐색
  size = size // 3
  reculsive(y, x, size)
  reculsive(y, x+size, size)
  reculsive(y, x+size+size, size)
  reculsive(y+size, x, size)
  reculsive(y+size, x+size, size)
  reculsive(y+size, x+size+size, size)
  reculsive(y+size+size, x, size)
  reculsive(y+size+size, x+size, size)
  reculsive(y+size+size, x+size+size, size)
  
reculsive(0,0,n)
print(count_1)
print(count_2)
print(count_3)