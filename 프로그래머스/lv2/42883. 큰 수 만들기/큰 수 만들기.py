def solution(number, k):
    
    # 스택 활용
    stack = []
    
    for n in number:
        # 빼주는 조건 생각
        while k > 0 and stack and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)
    
    # 빼주는 횟수가 남았다면 뒤부터 빼준다.
    if k > 0:
        stack = stack[:-k]
    
    # 출력
    return ''.join(stack)
        
    