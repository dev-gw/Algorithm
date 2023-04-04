import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr = sorted(arr)
print(arr[0], end=' ')
print(arr[N-1])