import sys

N = int(sys.stdin.readline())

for _ in range(N):
  arr = list(map(int, sys.stdin.readline().split()))
  arr = sorted(arr, reverse=True)
  print(arr[2])