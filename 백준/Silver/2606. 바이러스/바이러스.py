'''
1. 아이디어
 - bfs 한번 돌려서 개수확인, 자료구조 고려
2. 시간복잡도
 - 가능
3. 자료구조
 - 그래프정보 int[][], 방문여부 bool[][]
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(k):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
visited = [False] * (n+1)

# bfs
def bfs(v):
  result = 0
  q = deque()
  q.append(v)
  while q:
    now = q.popleft()
    if visited[now] == False:
      result += 1
      visited[now] = True
    for each in graph[now]:
      if visited[each] == False:
        q.append(each)
  return result - 1

print(bfs(1))