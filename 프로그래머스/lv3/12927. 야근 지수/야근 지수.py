import heapq
def solution(n, works):
    answer = 0
    hq = []
    if sum(works) <= n:
        return 0
    for work in works:
        heapq.heappush(hq,[-work,work])
    for i in range(n):
        h = heapq.heappop(hq)
        h[0] += 1
        h[1] -= 1
        heapq.heappush(hq,h)
    for q in hq:
        answer += q[1] ** 2
    return answer    