N = int(input())
C = list(map(int,input().split()))
M = int(input())

def calculate_new(new):
  request_sum = 0
  for c in C:
    request_sum += min(c,new)
  return request_sum

low = 0
good = -1
high = max(C)
while low <= high:
  new = (low + high) // 2
  if calculate_new(new) <= M:
    good = new
    low = new + 1
  else:
    high = new - 1

  ans = -1
  for c in C:
    given = min(c,good)
    ans = max(ans, given)
print(ans)