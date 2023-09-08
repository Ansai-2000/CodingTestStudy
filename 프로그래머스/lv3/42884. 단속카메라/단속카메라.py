def solution(routes):
    answer = 0
    routes.sort(key = lambda x:x[1])
    r = -30001
    for route in routes:
        if r < route[0]:
            answer += 1
            r = route[1]
    return answer        