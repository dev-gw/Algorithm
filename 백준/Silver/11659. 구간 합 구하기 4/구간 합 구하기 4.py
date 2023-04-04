import sys

N, M = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))

# Calculate psum
psum = [0] * N
psum[0] = nlist[0]
for i in range(0, N - 1):
  psum[i + 1] = psum[i] + nlist[i + 1]

# logic
for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  if a == 1:
    print(psum[b - 1])
  else:
    print(psum[b - 1] - psum[a - 2])