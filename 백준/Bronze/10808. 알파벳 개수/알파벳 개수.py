'''
1. 아이디어 - ASCII 코드
'''
s = input()

count = [0] * 26

for c in s:
  count[ord(c) - 97] += 1

for i in count:
  print(i, end=' ')