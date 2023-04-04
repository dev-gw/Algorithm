'''
1. 아이디어 - 그리디를 생각해야함, 남자를 인턴에 보내는게 유리
2. 시간복잡도
3. 자료구조 - 남은 학생 수 (int)
'''

N, M, K = map(int, input().split())
cnt = 0

for i in range(K):
  if (M*2) > N:
    M -= 1
  else:
    N -= 1
    
while N >= 2 and M >= 1:
  N -= 2
  M -= 1
  cnt += 1

print(cnt)