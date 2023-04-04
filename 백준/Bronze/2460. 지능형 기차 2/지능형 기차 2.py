import sys

cnt = 0
cnt_list = []
for _ in range(10):
  OUT, IN = map(int, sys.stdin.readline().split())
  cnt = cnt - OUT + IN
  cnt_list.append(cnt)
print(max(cnt_list))