'''
1. 아이디어
 - +1, -1, *2 의 경우의 수 확인, bfs 사용
2. 시간복잡도
3. 자료구조
'''
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False] * 100001
result = []

def bfs():
  q = deque()
  q.append((n, 0))
  while q:
    cur, count = q.popleft()
    if visited[cur] == False:
      visited[cur] = True
    if cur == k:
        result.append((cur, count))
    else:
      if 0<=cur+1<=100000 and visited[cur+1] == False:
        q.append((cur+1, count+1))
      if 0<=cur-1<=100000 and visited[cur-1] == False:
        q.append((cur-1, count+1))
      if 0<=cur*2<=100000 and visited[cur*2] == False:
        q.append((cur*2, count+1))

bfs()
answer = int(1e8)
cnt = 0
for each in result:
  answer = min(answer, each[1])
for each in result:
  if each[1] == answer:
    cnt += 1
print(answer)
print(cnt)