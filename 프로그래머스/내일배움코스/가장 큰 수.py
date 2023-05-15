'''
수를 늘려서 대소비교
'''
def solution(numbers):
    str_num = [str(x) for x in numbers]
    str_num.sort(key=lambda x: (x*4)[:4], reverse=True)
    if str_num[0] == '0':
        answer = '0'
    else:
        answer = ''.join(str_num)
    return answer
