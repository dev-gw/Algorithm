N, M = map(int, input().split())
result = []

# reculsive logic
def reculsive(start):
  # 종료조건
  if len(result) == M:
    print(" ".join(map(str, result)))
    return
  for i in range(start, N + 1):
    result.append(i)
    reculsive(i)
    result.pop()

reculsive(1)