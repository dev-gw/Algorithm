'''
1. 아이디어 - 완전탐색, 가능한 경우에서 노란색 칸 수 계산
'''

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    # 가능한 직사각형 반복
    for i in range(1, brown//2+1):
        if total % i == 0:
            # 가로, 세로
            hor = total // i
            ver = i
            # 체크
            if (hor - 2) * (ver - 2) == yellow:
                answer.append(hor)
                answer.append(ver)
                break
        
    return answer