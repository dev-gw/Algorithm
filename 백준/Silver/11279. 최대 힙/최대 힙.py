'''
1. 아이디어 - 최대 힙(자연수 x 넣고 0이면 출력)
'''

import heapq
import sys

# 입력
input = sys.stdin.readline
n = int(input())

# 배열
arr = []

# 연산
for _ in range(n):
  oper = int(input())
  if oper != 0:
    heapq.heappush(arr, -1 * oper)
  else:
    if not arr:
      print(0)
    else:
      answer = -1 * heapq.heappop(arr)
      print(answer)