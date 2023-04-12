'''
1. 아이디어
 - 단계마다 최솟값이 전체 최소로 이어짐(그리디)
 - 바구니의 범위를 비교하면서 칸 수 더해가기

2. 시간복잡도
 - O(J)

3. 자료구조
 - 바구니 왼쪽, 오른쪽
'''

import sys
input = sys.stdin.readline

# 입력받기
n, m = map(int, input().split())
j = int(input())
arr = [0]
for _ in range(j):
  arr.append(int(input()))

# 초기 바구니
left = 1
right = left + m - 1

# 단계 반복
sum = 0
for i in range(1, len(arr)):
  apple = arr[i]
  # 바구니에 바로 가는경우
  if left <= apple <= right:
    continue
  # 바구니 왼쪽으로 떨어지는 경우
  if apple < left:
    # 바구니 옮기기
    sum += left - apple
    left = apple
    right = left + m - 1
  # 바구니 오른쪽으로 떨어지는 경우
  elif apple > right:
    # 바구니 옮기기
    sum += apple - right
    right = apple
    left = right - m + 1

print(sum)