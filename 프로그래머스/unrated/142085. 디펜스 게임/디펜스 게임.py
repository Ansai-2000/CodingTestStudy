import heapq
def solution(n, k, enemy):
    answer = 0
    s = []
    i = 0
    while i<len(enemy):
        heapq.heappush(s,(-enemy[i],enemy[i]))
        n -= enemy[i]
        if n < 0:
            h = heapq.heappop(s)[1]
            n += h
            k -= 1
            if k < 0:
                break
        i += 1        
    return i