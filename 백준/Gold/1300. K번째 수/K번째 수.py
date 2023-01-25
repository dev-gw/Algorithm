# input
N = int(input())
K = int(input())


# return small
def small(new):
  j = 0
  for i in range(1, N + 1):
    j += min(N, (new - 1) // i) ## issue 1
  return j


# return big
def big(new):
  j = 0
  for i in range(1, N + 1):
    j += N - min(N, new // i)
  return j


# iteration
low = 1
high = min(N * N, int(1e9))
answer = -1
while low <= high: ## issue 2
  new = (low + high) // 2
  if small(new) > K - 1:
    high = new - 1
  elif big(new) > N * N - K:
    low = new + 1
  else:
    answer = new
    break
print(answer)