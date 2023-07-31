import math
def solution(fees, records):
    answer = []
    dic = dict()
    dic2 = dict()
    for record in records:
        time,num,inout = record.split()
        h,m = time.split(":")
        minute = int(h)*60 + int(m)
        num = record[6:10]
        if inout == "OUT":
            try:
                dic2[num] += minute - dic[num]
            except:
                dic2[num] = minute - dic[num]
            del dic[num]    
        else:
            dic[num] = minute


    for num,minute in dic.items():
        if num in dic2:
            dic2[num] += 1439 - dic[num]
        else:
            dic2[num] = 1439 - dic[num]
    
    for d in dic2.items():
        if dic2[d[0]] >= fees[0]:
            dic2[d[0]] = fees[1] + math.ceil((dic2[d[0]] - fees[0])/fees[2]) * fees[3]
        else:
            dic2[d[0]] = fees[1]
    
    dic2 = sorted(dic2.items(), key = lambda x:x[0])     
    for i in dic2:
        answer.append(i[1])
    return answer    