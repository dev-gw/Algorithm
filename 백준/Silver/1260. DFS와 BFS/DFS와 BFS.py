'''
1. 아이디어
 - dfs, bfs, 정점번호가 작은 것 먼저 방문을 구현?
 
2. 시간복잡도
 - O(V+E) + 정렬
 
3. 자료구조
 - 그래프 정보 int[][], 방문여부 bool [], dfs 재귀, bfs 큐(deque)
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
visited_d = [False] * (n+1)
visited_b = [False] * (n+1)

# dfs
def dfs(v):
  if visited_d[v] == False:
    visited_d[v] = True
    print(v, end=' ')
    for each in sorted(graph[v]):
      if visited_d[each] == False:
        dfs(each)

# bfs
def bfs(v):
  q = deque()
  q.append(v)
  while q:
    n = q.popleft()
    if visited_b[n] == False:
      print(n, end=' ')
      visited_b[n] = True
      for each in sorted(graph[n]):
        if visited_b[each] == False:
          q.append(each)
          
# logic
dfs(v)
print()
bfs(v)