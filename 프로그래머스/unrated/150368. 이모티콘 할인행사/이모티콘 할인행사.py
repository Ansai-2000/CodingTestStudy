import itertools
def solution(users, emoticons):
    answer = []
    p = list(itertools.product([10,20,30,40],repeat=len(emoticons)))
    arr = []
    for i in range(len(p)):
        cnt = 0
        s = 0
        for user in users:
            u = 0
            for j in range(len(p[i])):
                if user[0] <= p[i][j]:
                    u += emoticons[j] * (1 - p[i][j] / 100)
            if user[1] <= u:
                cnt += 1
            else:
                s += u
        answer.append([cnt,s])            
    answer.sort(key = lambda x:(-x[0],-x[1]))
    return answer[0]
    