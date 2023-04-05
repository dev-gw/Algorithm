'''
1. 아이디어
 - +1, -1, *2 의 경우의 수 확인, bfs 사용, 방문여부에 depth를 표기해준다면 바로 확인가능
2. 시간복잡도
3. 자료구조
'''
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [0] * 100001
node = [0] * 100001

# route
def route(x):
  arr = []
  temp = x
  for _ in range(visited[x]+1):
    arr.append(temp)
    temp = node[temp]
  print(' '.join(map(str, arr[::-1])))

# bfs
def bfs(x):
  q = deque()
  q.append(x)
  while q:
    now = q.popleft()
    if now == k:
      print(visited[now])
      route(now)
      return
    # 다음 수 탐색
    for next in (now+1, now-1, now*2):
      if 0<=next<=100000 and visited[next] == 0:
        # 방문처리(depth 이용)
        visited[next] = visited[now] + 1
        q.append(next)
        node[next] = now

bfs(n)