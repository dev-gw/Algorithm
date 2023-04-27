'''
1. 아이디어 - dfs 백트래킹으로 경우의 수 탐색
'''
def dfs(numbers, target, n, depth):
    global answer
    # 종료조건
    if depth == len(numbers):
        if n == target:
            answer += 1
        return
    dfs(numbers, target, n + numbers[depth], depth + 1)
    dfs(numbers, target, n - numbers[depth], depth + 1)

        
def solution(numbers, target):
    global answer
    answer = 0
    
    dfs(numbers, target, 0, 0)
    
    return answer