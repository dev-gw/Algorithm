'''
스택을 활용해도 시간복잡도 차이가 없을 것 같음
'''
def solution(prices):
    answer = []
    for i in range(0, len(prices)-1):
        sec = 0
        for j in range(i+1, len(prices)):
            sec += 1
            if prices[i] > prices[j]:
                answer.append(sec)
                break
        else:
            answer.append(sec)
        
    answer.append(0)
    return answer