import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# logic
result = 0
for i in arr:
  if i == 1:
    continue
  elif i == 2:
    result += 1
  else:
    reminder = []
    for j in range(2, i):
      reminder.append(i % j)
    if 0 not in reminder:
      result += 1
print(result)