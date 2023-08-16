import itertools
def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    combi = []
    for i in range(1,col+1):
        combi.extend(itertools.combinations(range(col),i))
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]
        tmp = []
        for item in relation:
            t = ()
            for key in i:
                t = t + (item[key],)
            tmp.append(t)    
        if len(set(tmp)) == row:
            put = True
            for x in unique:
                if set(x).issubset(set(i)):
                    put = False
                    break
            if put:
                unique.append(i)        
    return len(unique)            