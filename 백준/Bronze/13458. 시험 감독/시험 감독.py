import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

result = n
for each in a:
  each -= b
  if each > 0:
    if each % c:
      result += (each // c) + 1
    else:
      result += (each // c)
      
print(result)