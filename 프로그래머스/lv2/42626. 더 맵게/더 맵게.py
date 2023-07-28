from heapq import *
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while(scoville[0] < K):    
        if len(scoville) == 1:
            return -1
        a = heappop(scoville)
        b = heappop(scoville)
        heappush(scoville,a+b*2)
        answer+=1
    return answer