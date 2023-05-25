'''
제일 낮은 숫자 먼저 확인하고 섞기
'''
import heapq
def solution(scoville, K):
    
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K and len(scoville) > 1:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        answer += 1
        
    if len(scoville) == 1 and scoville[0] < K:
        return -1
    else:
        return answer