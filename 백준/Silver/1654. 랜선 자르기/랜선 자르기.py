'''
1. 아이디어
 - 잘라야 하는 길이 이분탐색

2. 시간복잡도
 - O(K * 이분탐색)
'''

import sys

input = sys.stdin.readline

# 입력받기
k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

# 이분탐색
left = 1
right = max(arr)
answer = -1

while left <= right:
  # 새로운 값
  mid = (left + right) // 2

  # 만들어지는 개수 계산
  count = 0
  for each in arr:
    if each >= mid:
      count = count + (each // mid)

  # 필요한 개수보다 더 만들어지는 경우
  if count >= n:
    left = mid + 1
    answer = mid
  # 필요한 개수가 부족한 경우
  else:
    right = mid - 1

print(answer)