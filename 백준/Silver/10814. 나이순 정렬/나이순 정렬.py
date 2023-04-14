n = int(input())

data = []
for i in range(n):
  a, b = input().split()
  data.append((int(a), b, i))

# 정렬
data.sort(key = lambda x: (x[0], x[2]))

# 출력
for each in data:
  print(each[0], end=' ')
  print(each[1])