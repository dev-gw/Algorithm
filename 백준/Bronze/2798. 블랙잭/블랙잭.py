'''
1. 아이디어
 - 조합을 이용하거나 반복문으로 탐색해도 됌(n-2번만)
2. 시간복잡도
 - O(N^2)
'''
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 조합
max = 0
comb = combinations(arr, 3)
for each in comb:
  if max < sum(each) <= m:
    max = sum(each)
print(max)