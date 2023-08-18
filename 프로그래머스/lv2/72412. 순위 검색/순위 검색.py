from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    answer = []
    info_dict = {}
    for i in range(len(info)):
        il = info[i].split()
        k = il[:-1]
        v = il[-1]
        for j in range(5):
            for c in combinations(k,j):
                tmp = "".join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(v))
                else:
                    info_dict[tmp] = [int(v)]
    for k in info_dict:
        info_dict[k].sort()
    for q in query:
        ql = q.split()
        k = ql[:-1]
        v = ql[-1]
        while "and" in k:
            k.remove("and")
        while '-' in k:
            k.remove('-')
        k = "".join(k)    
        if k in info_dict:
            scores = info_dict[k]
            if scores:
                enter = bisect_left(scores,int(v))
                answer.append(len(scores)-enter)
        else:
            answer.append(0)
    return answer