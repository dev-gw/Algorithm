def solution(N, number):
    # set
    s = [set() for _ in range(8)]
    for i, x in enumerate(s, start=1):
        x.add(int(str(N)*i))
    
    # 집합 탐색
    for i in range(len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        # 타겟 확인
        if number in s[i]:
            answer = i + 1
            break
    # 타겟이 없다면
    else:
        return -1
    return answer