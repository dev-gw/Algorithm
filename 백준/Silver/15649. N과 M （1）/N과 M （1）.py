N, M = map(int, input().split())

visited = [False] * (N+1)
result = []

# Reculsive
def reculsive(num):
  # 종료조건 - 깊이가 같아질때
  if num == M:
    print(' '.join(map(str, result)))
    return
    
  for i in range(1, N+1):
    if visited[i] == False:
      visited[i] = True
      result.append(i)
      reculsive(num+1)
      visited[i] = False
      result.pop()

reculsive(0)