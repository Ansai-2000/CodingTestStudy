def solution(n, l, r):
    answer = 0
    for i in range(l-1,r):
        flag = True
        while i != 0:
            if i % 5 == 2:
                flag = False
                break
            i = i//5 
        if flag:
            answer +=1
    return answer