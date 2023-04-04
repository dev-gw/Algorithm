import sys

T = int(sys.stdin.readline())

# logic
for _ in range(T):
  n = int(sys.stdin.readline())
  location = 0
  while n != 0:
    a = n // 2
    b = n % 2
    if b == 1:
      print(location, end=' ')
    n = a
    location += 1