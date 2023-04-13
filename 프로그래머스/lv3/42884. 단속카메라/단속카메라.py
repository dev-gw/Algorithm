def solution(routes):
    cnt = 0
    key = -300001
    
    # 정렬
    routes.sort(key = lambda x: x[1])
    
    for each in routes:
        # 단속이 걸리지 않는경우
        if each[0] > key:
            cnt += 1
            key = each[1]

    return cnt