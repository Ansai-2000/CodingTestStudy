def solution(number, limit, power):
    answer = []
    for i in range(1,number+1):
        cnt = 0
        for a in range(1,int(i**0.5)+1):
            if(i**0.5==a):
                cnt += 1
            elif(i % a == 0):
                cnt += 2
            if(cnt>limit):
                break
        if(cnt>limit):
            answer.append(power)
        else:
            answer.append(cnt)
    return sum(answer)