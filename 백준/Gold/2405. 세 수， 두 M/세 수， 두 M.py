import sys

# Data input
N = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for _ in range(N)]

# mean, median function
def calc(a, b, c):
  ## mean * 3 = (a+b+c)
  return abs((a + b + c) - (3 * b))

# sort
n_list.sort()

# logic
answer = -1
for i in range(1, N - 1):  # first and last cannnot be answer
  # 최소부분
  answer = max(answer, calc(n_list[0], n_list[i], n_list[i + 1]))
  # 최대부분
  answer = max(answer, calc(n_list[i - 1], n_list[i], n_list[N - 1]))
print(answer)