'''
1.아이디어
 - DFS 재귀, 4방향 이동, 매번 DFS마다 개수 세기
2. 시간복잡도
 - O(V+E) -> N^2 + 4N^2 = O(N^2)
3. 자료구조
 - 그래프 int[][], 방문여부 bool[][]
'''

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
cnt = 0

# dfs
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def dfs(y, x):
    global cnt
    cnt += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<n and 0<=nx<n:
            if graph[ny][nx] == 1 and visited[ny][nx] == False:
                visited[ny][nx] = True
                dfs(ny, nx)

# logic
result = []
for j in range(n):
    for i in range(n):
        cnt = 0
        if graph[j][i] == 1 and visited[j][i] == False:
            visited[j][i] = True
            dfs(j,i)
            result.append(cnt)

result.sort()
print(len(result))
for i in result:
    print(i)