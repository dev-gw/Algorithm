'''
1. 아이디어
 - 4등분을 해가면서 재귀탐색, 조건에 맞으면 탈출
2. 시간복잡도
 - O(N^3) - 그래프 탐색 * 재귀 횟수
3. 자료구조
 - 그래프 정보 int[][]
'''

import sys
input = sys.stdin.readline

# 영상의 크기와 그래프 정보 입력
n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

# 압축가능한지 확인
def check(y, x, n):
  check = graph[y][x]
  for j in range(y, y + n):
    for i in range(x, x + n):
      if graph[j][i] != check:
        return False
  return True

# reduction(시작점과 사이즈만 알면 가능)
def reduction(y, x, n):
  # 그래프가 압축되지 않는다면
  if check(y,x,n) == False:
    # 4등분
    print('(', end='')
    n = n // 2
    reduction(y, x, n)
    reduction(y, x+n, n)
    reduction(y+n, x, n)
    reduction(y+n, x+n, n)
    print(')', end='')

  # 그래프가 압축된다면
  else:
    print(graph[y][x], end='')
    
reduction(0,0,n)