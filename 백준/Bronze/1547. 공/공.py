n = int(input())
arr = [1,2,3]

for _ in range(n):
  a, b = map(int, input().split())
  index_a = arr.index(a)
  index_b = arr.index(b)
  arr[index_a], arr[index_b] = arr[index_b], arr[index_a]

print(arr[0])