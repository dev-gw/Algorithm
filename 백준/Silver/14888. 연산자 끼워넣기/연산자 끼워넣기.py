'''
1.아이디어
 - 백트래킹 탐색, DFS, 연산자 불러오는것 고려
2. 시간복잡도
 - O(N(N-1)) -> O(N^2)
3. 자료구조
'''
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
operator = list(map(int, input().split()))
max = -int(1e8)
min = int(1e8)

# dfs
def dfs(result, depth):
  global min, max
  # 종료조건
  if depth == n:
    if result < min:
      min = result
    if result > max:
      max = result
    return
  # 반복
  for i in range(4):
    if operator[i] == 0:
      continue
    if i == 0:
      operator[i] -= 1
      dfs(result + a[depth], depth+1)
      operator[i] += 1
    if i == 1:
      operator[i] -= 1
      dfs(result - a[depth], depth+1)
      operator[i] += 1
    if i == 2:
      operator[i] -= 1
      dfs(result * a[depth], depth+1)
      operator[i] += 1
    if i == 3:
      operator[i] -= 1
      if result < 0:
        dfs(-(abs(result) // a[depth]), depth+1)
      else:
        dfs(result // a[depth], depth+1)
      operator[i] += 1

dfs(a[0], 1)
print(max)
print(min)