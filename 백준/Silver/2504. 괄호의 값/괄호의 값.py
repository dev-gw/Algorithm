# 스택
# temp를 이용한 계산
# 괄호 확인을 위해 stack과 input모두 활용해야함

sen = input()
stack = []
result = 0
temp = 1

for i in range(len(sen)):
  s = sen[i]
  if s == '(':
    stack.append(s)
    temp *= 2

  elif s == '[':
    stack.append(s)
    temp *= 3

  elif s == ')':
    if len(stack) == 0 or stack[-1] == '[':
      result = 0
      break
    else:
      if sen[i-1] == '(':
        result += temp
      stack.pop()
      temp //= 2

  elif s == ']':
    if len(stack) == 0 or stack[-1] == '(':
      result = 0
      break
    else:
      if sen[i-1] == '[':
        result += temp
      stack.pop()
      temp //= 3
      
if len(stack) == 0:
  print(result)
else:
  print(0)