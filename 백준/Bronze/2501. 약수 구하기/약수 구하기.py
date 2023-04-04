import sys
N, K = map(int, sys.stdin.readline().split())

# logic
answer = []
for i in range(1, N+1):
  if N % i == 0: answer.append(i)
answer = sorted(answer)

print(0) if len(answer) < K else print(answer[K - 1]) 