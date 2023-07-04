def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        s = ""
        cnt = i
        for j in range(len(p)):
            s += t[cnt]
            cnt += 1
        if(int(s)<=int(p)):
            answer+=1
    return answer