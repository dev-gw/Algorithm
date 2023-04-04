import sys
from itertools import combinations

H = [int(sys.stdin.readline()) for _ in range(9)]

# logic
H_list = combinations(H, 7)
for i in H_list:
  if sum(i) == 100:
    for j in sorted(i):
      print(j)
    break