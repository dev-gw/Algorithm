N, M = map(int, input().split())

# logic
arr = []
cnt = 1 
while len(arr) <= M:
  for _ in range(cnt):
    arr.append(cnt)
  cnt += 1
print(sum(arr[N-1:M]))