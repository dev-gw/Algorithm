import sys

input = sys.stdin.readline

# 입력받기
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 초기값
answer = []
sum = 0
for i in range(k):
  sum += arr[i]
answer.append(sum)

# 슬라이딩 탐색
for j in range(k, n):
  answer.append(answer[-1] - arr[j-k] + arr[j])

print(max(answer))