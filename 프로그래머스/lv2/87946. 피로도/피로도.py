from itertools import permutations
def solution(k, dungeons):
    all_dungeons = []
    for i in permutations(dungeons,len(dungeons)):
        all_dungeons.append(list(i))
    possible = []
    i = 0
    while i < len(all_dungeons):
        s = k
        cnt = 0
        for j in all_dungeons[i]:
            if s >= j[0]:
                s = s - j[1]
                cnt += 1
            elif s < j[0]:
                break
        possible.append(cnt)        
        i += 1
    answer = max(possible)    
    return answer