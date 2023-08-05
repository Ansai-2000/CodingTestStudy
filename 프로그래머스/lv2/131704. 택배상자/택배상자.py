from collections import deque
def solution(order):
    answer = 0
    main = deque()
    main = deque([i for i in range(1,len(order)+1)])
    main.append(0)
    sub = deque()
    i = 0
    while main and i < len(order):
        if order[i] == main[0]:
            answer+=1
            i+=1
            main.popleft()
        elif sub and order[i] == sub[-1]:
            answer+=1
            i+=1
            sub.pop()
        else:
            sub.append(main.popleft())
    return answer