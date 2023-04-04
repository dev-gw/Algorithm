N, M = map(int, input().split())
result = []

# reculsive logic
def reculsive(start):
  if len(result) == M:
    print(' '.join(map(str, result)))
  for i in range(start, N+1):
    #if i not in result:
    result.append(i)
    reculsive(i+1)
    result.pop()

reculsive(1)