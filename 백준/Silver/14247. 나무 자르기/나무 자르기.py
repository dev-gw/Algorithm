import sys

# input
n = int(sys.stdin.readline())
H = list(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))
I = list(range(n))  # index list

# Sorting I by A
I = sorted(I, key=lambda i: A[i])

# Logic
answer = 0
for i in range(n):
  index = I[i]
  answer += (A[index] * i) + H[index]

print(answer)