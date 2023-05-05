'''
1. 아이디어 - 큐(리스트)
'''

def solution(priorities, location):
    
    # 프로세스 리스트
    process = []
    for i in range(len(priorities)):
        process.append((i, priorities[i]))
    
    # 구하고자 하는 프로세스
    answer = process[location][0]
    print('answer', answer)
    count = 0
    
    while process:
        # 중요도 비교
        now = process.pop(0)
        print('now', now)
        print(count)
        switch = 0
        # 실행가능한지
        for each in process:
            if each[1] > now[1]:
                switch = 1
                break
        # 중요도가 높은게 있다면
        if switch == 1:
            process.append(now)
        else:
            count += 1
            if now[0] == answer:
                return count
            