'''
1. 아이디어 - 스택(해당 숫자보다 작은 숫자는 빼기), 남은 스택도 빼기
2. 시간복잡도 - O(N)
'''

def solution(progresses, speeds):
    answer = []
    count = 0
    stack = []
    
    for i in range(len(progresses)):
        # 남은 일수 계산
        if (100 - progresses[i]) % speeds[i] == 0:
            remain = (100 - progresses[i]) // speeds[i]
        else:
            remain = (100 - progresses[i]) // speeds[i] + 1
        # 스택 비교
        while stack and stack[0] < remain:
            stack.pop()
            count += 1
        # 스택 추가
        stack.append(remain)
        # 배포작업이 이루어진 경우
        if count > 0:
            answer.append(count)
            count = 0
    # 남아있는 스택 처리
    if stack:
        answer.append(len(stack))
    
    return answer
