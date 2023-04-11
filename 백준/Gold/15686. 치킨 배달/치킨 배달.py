'''
1. 아이디어
 - 그래프를 전체 탐색하면서 빈칸에 위치와 집에 위치를 리스트에 담기
 - 빈칸에 위치를 조합 후 집과의 거리 계산
 - 최솟값을 갱신

2. 시간복잡도
 - O(N^2 + M + 조합 시간)

3. 자료구조
 - 그래프 정보 int[][], 빈칸 정보 [()], 집 정보 [()]
'''

import sys
from itertools import combinations
input = sys.stdin.readline

# 입력 받기(m - 치킨집)
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 치킨집 정보
chicken = []
# 집 정보
house = []

# main
# 그래프 탐색
for j in range(n):
  for i in range(n):
    if graph[j][i] == 0:
      continue
    if graph[j][i] == 2:
      chicken.append([j, i])
    elif graph[j][i] == 1:
      house.append([j, i])

# 선택가능한 치킨집 조합
combi_chicken = combinations(chicken, m)

answer = []
# 경우의 수 탐색
# 치킨집 조합 하나
for each_chicken in combi_chicken:
  city_dist = 0
  # 각 집에 최소거리
  for each_house in house:
    house_dist = int(1e8)
    for chick in each_chicken:
      house_dist = min(house_dist, abs(each_house[0] - chick[0]) + abs(each_house[1] - chick[1]))
    # 조합 하나당 도시 거리
    city_dist += house_dist
  answer.append(city_dist)
    
print(min(answer))