def solution(n, words):
    num = 0
    cnt = 0
    s = []
    for i in range(len(words)):
        s.append(words[i])
        if i == 0:
            continue
        if words[i-1][-1] != words[i][0]:
            num = i%n + 1
            cnt = (i) // n + 1
            break
        if s.count(words[i]) == 2:
            num = i % n + 1
            cnt = (i) // n + 1
            break
    if cnt == 0:
        return [0,0]
    else:
        return num,cnt