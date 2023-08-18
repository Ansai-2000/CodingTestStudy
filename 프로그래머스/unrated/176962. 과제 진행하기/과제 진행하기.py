def solution(plans):
    answer = []
    for plan in plans:
        plan[1] = convertor(plan[1])
        plan[2] = int(plan[2])
    plans.sort(key = lambda x : x[1])
    
    stack = []
    for i in range(len(plans)):
        if i == len(plans)-1:
            stack.append(plans[i])
            break
        sub,st,t = plans[i]
        nsub,nst,nt = plans[i+1]
        if st + t <= nst:
            answer.append(sub)
            temp_time = nst - (st+t)
            
            while temp_time != 0 and stack:
                tsub, tst, tt = stack.pop()
                if temp_time >= tt:
                    answer.append(tsub)
                    temp_time -= tt
                else:
                    stack.append([tsub,tst,tt - temp_time])
                    temp_time = 0
        else:
            plans[i][2] = t - (nst - st)
            stack.append(plans[i])
    while stack:
        sub,st,tt = stack.pop()
        answer.append(sub)
    return answer    
    
def convertor(a):
    m,s = a.split(":")
    return int(m) * 60 + int(s)