'''
정렬 조건 생각
'''

def solution(numbers):
    str_num = [str(x) for x in numbers]
    # 정렬
    str_num.sort(key=lambda x: (x*4)[:4], reverse=True)
    
    if str_num[0] =='0':
        return '0'

    return ''.join(str_num)