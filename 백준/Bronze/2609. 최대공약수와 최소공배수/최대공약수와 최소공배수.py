import sys

# reculsive
def gcd(N, M):
  if N % M == 0:
    return M
  else:
    return gcd(M, N % M)

# logic
N, M = map(int, sys.stdin.readline().split())
gcd = gcd(N, M)
lcm = (N * M) // gcd
print(gcd)
print(lcm)