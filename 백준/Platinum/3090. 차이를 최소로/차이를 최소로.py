# input
N, T = map(int, input().split(" "))
A = list(map(int, input().split(" ")))


# calculation count
def cal_count(input_list, new):
  count = 0
  for i in range(N-1):
    if input_list[i+1] - input_list[i] > new:
      count += input_list[i+1] - input_list[i] - new ## issue 1
      input_list[i + 1] = input_list[i] + new
  for j in range(N-1, 0, -1):
    if input_list[j - 1] - input_list[j] > new:
      count += input_list[j - 1] - input_list[j] - new
      input_list[j - 1] = input_list[j] + new
  return input_list, count

# iteration
low = 0
high = max(A)
answer = -1
while low <= high:
  new = (low + high) // 2
  cand = A.copy()
  answer_list, count = cal_count(cand, new)
  if count <= T:
    answer = new
    high = new - 1
  else:
    low = new + 1
    
# Answer
print(" ".join(list(map(str,answer_list))))