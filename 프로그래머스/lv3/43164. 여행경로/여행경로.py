def solution(tickets):
    # dictionary
    dict = {}
    for each in tickets:
        dict[each[0]] = dict.get(each[0], []) + [each[1]]
    # 정렬
    for r in dict:
        dict[r].sort()

    # dfs
    stack = ["ICN"]
    answer = []
    while stack:
        top = stack[-1]
        # 갈 수 없는 경우
        if top not in dict or len(dict[top]) == 0:
            answer.append(stack.pop())
        # 경로 추가
        else:
            stack.append(dict[top][0])
            dict[top] = dict[top][1:]
    answer.reverse()

    return answer