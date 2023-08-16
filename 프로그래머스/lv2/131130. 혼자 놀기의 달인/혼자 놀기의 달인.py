def solution(cards):
    answer = 0
    for i in range(len(cards)):
        a = dfs(cards,[],i)
        la = len(a)
        if la == len(cards):
            return 0
        for j in range(len(cards)):
            if cards[j] in a:
                continue
            else:
                b = dfstwo(cards,a,[],j) 
                lb = len(b)
                answer = max(answer,la*lb)    
    return answer

def dfs(cards,stack,num):
    s = cards[num]
    if s in stack:
        return stack
    stack.append(s)
    return dfs(cards,stack,s-1)

def dfstwo(cards,stack1,stack2,num):
    s = cards[num]
    if s in stack1 or s in stack2:
        return stack2
    stack2.append(s)
    return dfstwo(cards,stack1,stack2,s-1)