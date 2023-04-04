'''
1. 아이디어 -> 고인다는 것의 의미파악이 중요
2. 시간복잡도 -> O(HW), 가능
3. 자료구조 -> int[][], cnt
'''

import sys
input = sys.stdin.readline

H, W = map(int, input().split())
block = list(map(int, input().split()))

array = list([0] * W for _ in range(H))
cnt = 0

# simulation
for i in range(1, W-1):
  left = max(block[0:i])
  right = max(block[i+1:W])
  if min(left, right) - block[i] > 0:
    cnt += min(left, right) - block[i]
print(cnt)