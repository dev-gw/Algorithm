N, M = map(int, input().split())
result = []

# reculsive logic
def reculsive():
  # 종료조건
  if len(result) == M:
    print(" ".join(map(str, result)))
    return
  for i in range(1,N+1):
    result.append(i)
    reculsive()
    result.pop()

reculsive()