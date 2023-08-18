def solution(begin, end):
    answer = []
    for i in range(begin,end+1):
        if i == 1:
            answer.append(0)
            continue
        else:
            k = 1
        tmp = []
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                k = i//j
                if k<=10**7:
                    tmp.append(k)
                    break
                else:
                    tmp.append(j)
        if tmp:
            answer.append(tmp[-1])
        else:
            answer.append(1)
    return answer