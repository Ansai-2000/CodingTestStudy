def solution(s):
    answer = 1001
    for i in range(1,len(s)+1):
        m = 1
        a = s[:i]
        c = ""
        for j in range(i,len(s),i):
            if a == s[j:i+j]:
                m += 1
            else:
                if m == 1:
                    c += a
                else:
                	c += str(m) + a
                a = s[j:j+i]
                m = 1
        if m==1:
            c += a
        else:
            c += str(m) + a
        answer = min(len(c),answer)
    return answer