tmp = "0123456789"
def solution(n):
    answer = ''
    s = com(n,3)    
    s = s.replace("0","4")

    return s

def com(n,k):
    q = n//k
    r = n%k
    if n == 0:
        return ""
    if r == 0:
        q-=1
    return com(q,k) + tmp[r]