import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  r, s = input().split()
  for each in s:
    for _ in range(int(r)):
      print(each, end='')
  print()