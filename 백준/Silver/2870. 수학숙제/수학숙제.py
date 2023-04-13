'''
1. 아이디어 - 스택 활용, 스택에서 빼는 조건 생각
2. 시간복잡도 - O(N)
3. 자료구조 - 숫자를 담는 리스트, 스택
'''

import sys
input = sys.stdin.readline

# n 입력
n = int(input())

# 숫자 리스트
figure = []
sentence = []

# main
for _ in range(n):
  sentence.append(input())

for each in sentence:
  stack = []
  for s in each:
    
    # 숫자인경우
    if s.isdigit():
      stack.append(s)
      
    # 문자인경우
    else:
      if stack:
        figure.append(int(''.join(stack)))
        stack = []
      
# 정렬
figure.sort()

# 출력
for each in figure:
  print(each)