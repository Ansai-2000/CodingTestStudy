import heapq
def minmaxheap(hq):
    queue = []
    for num in hq:
        heapq.heappush(queue,-num)
    return queue    
def solution(operations):
    answer = []
    minq = []
    maxq = []
    for oper in operations:
        op,num = oper.split()
        num = int(num)
        if op == 'I':
            heapq.heappush(minq,num)
            heapq.heappush(maxq,-num)
        elif op == 'D':
            if minq: 
            	if num == -1:
                    heapq.heappop(minq)
                    maxq = minmaxheap(minq)
            	else:
                    heapq.heappop(maxq)     
                    minq = minmaxheap(maxq)
    
    if minq:
        return [-maxq[0],minq[0]]
    else:
        return [0,0]