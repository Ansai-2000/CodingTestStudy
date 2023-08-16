def solution(k, ranges):
    answer = []
    area = [0.0]
    while k!=1:
        newK = (k//2) if k % 2 == 0 else (k*3+1)
        minY,maxY = min(k,newK),max(k,newK)
        area.append(area[-1] + ((1/2) * (maxY+minY)))
        k = newK
    n = len(area)    
    for y1,y2 in ranges:
        if n + y2 - 1 >= y1:
            answer.append(area[y2-1] - area[y1])
        else:
            answer.append(-1)
    return answer        