'''
1. 시간의 범위를 따져서 포함되는지 확인 - x
2. 시간이 겹쳐서 방이 필요할 때만 +1 
'''
# 시간 -> 분
def time2minute(book_time):
    temp = book_time
    for i, x in enumerate(temp):
        temp[i][0] = int(x[0][0:2])*60 + int(x[0][3:5])
        temp[i][1] = int(x[1][0:2])*60 + int(x[1][3:5]) + 10
    return temp


def solution(book_time):
    book_minute = time2minute(book_time)
    
    # 24시간 확인
    answer = 0
    for i in range(60*24):
        cnt = 0
        for each in book_minute:
            start, end = each
            if start <= i < end:
                cnt += 1
        if cnt > answer:
            answer = cnt
    return answer