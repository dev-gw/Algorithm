'''
1. 아이디어
 - 그리디(앞번호부터 확인)
 - N이 작을 경우 전체 반복 가능
 - N에 비해 체육복을 빌려줄 사람이 적다면 set 이용
2. 시간복잡도
 - O(KlogK)
3. 자료구조
 - set
'''
def solution(n, lost, reserve):
    # 여분을 가져왔으나 도난
    s = set(reserve) & set(lost)
    # 빌려야하는사람
    l = set(lost) - s
    # 빌려줄 수 있는사람
    r = set(reserve) - s
    
    # 빌려주기
    for i in r:
        if (i-1) in l:
            l.remove(i-1)
        elif (i+1) in l:
            l.remove(i+1)
    answer = n - len(l)
    
    return answer
