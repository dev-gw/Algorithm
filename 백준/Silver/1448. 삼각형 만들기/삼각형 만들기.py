import sys

N = int(sys.stdin.readline())
N_list = [int(sys.stdin.readline()) for _ in range(N)]

# Logic
answer = -1
N_list.sort()
for i in range(N - 1, 1, -1):
  if N_list[i] < N_list[i - 1] + N_list[i - 2]:
    answer = N_list[i] + N_list[i - 1] + N_list[i - 2]
    break
print(answer)