'''
1. 아이디어
 - 이분탐색으로 H에 따라 가져갈 수 있는 M을 구한다.
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

tree = list(map(int, input().split()))

# 이분탐색 (h의 범위)
left = 0
right = max(tree)

while left < right:
  mid = (left + right) // 2
  if left == mid:
    break
  # 구해지는 나무의 양
  sum = 0
  for each in tree:
    if each > mid:
      sum += (each - mid)
  # 가져가려는 나무보다 작다면
  if sum < m:
    right = mid
  # 가져가려는 나무보다 많다면
  else:
    left = mid

print(mid)