import sys

N = int(sys.stdin.readline())

cum = [0, 1]
for i in range(2, N+1):
  new = cum[i-2] + cum[i-1]
  cum.append(new)
print(cum[N])