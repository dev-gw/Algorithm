'''
1. 아이디어 - 동전이 배수기 때문에 항상 큰 가치부터 처리
2. 시간복잡도 - O(N)
3. 자료구조
'''


import sys

input = sys.stdin.readline
N, K = map(int, input().split())
values = [int(input()) for _ in range(N)]
values.sort(reverse=True)
cnt = 0

# Greedy
for value in values:
  cnt += K // value
  K = K % value

print(cnt)