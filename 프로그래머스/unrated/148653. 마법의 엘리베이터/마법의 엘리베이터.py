def solution(storey):
    answer = 0
    cnt = 1
    while storey != 0:
        s = round(storey,-cnt)
        print(storey,s)
        answer += po(abs(storey - s))
        storey = s
        cnt += 1
    return answer    

def po(a):
    b = 10
    while True:
        if a // b == 0:
            return a // (b/10)
        b *= 10