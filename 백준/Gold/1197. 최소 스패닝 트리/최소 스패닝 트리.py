'''
1. 아이디어 - mst(prim), heap 사용, 작은 비용부터 꺼내기
2. 시간복잡도 - O(ElogE)
3. 자료구조 - 인접리스트 int[][][], 방문여부 chk
'''
import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
edge = [[] for _ in range(V+1)]
chk = [False] * (V+1)
result = 0

for i in range(E):
  A, B, C = map(int, input().split())
  edge[A].append([C,B])
  edge[B].append([C,A])

# logic - prim
heap = [[0,1]]
while heap:
  cost, node = heapq.heappop(heap)
  if chk[node] == False:
    chk[node] = True
    result += cost
    for next_node in edge[node]:
      if chk[next_node[1]] == False:
        heapq.heappush(heap, next_node)

print(result)