from collections import deque
def solution(queue1, queue2):
    s1 = sum(queue1)
    s2 = sum(queue2)
    l = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    s = (s1+s2)/2
    answer = 0
    while queue1 and queue2 and s1 != s2:
        if s1 > s2:
            p = queue1.popleft()
            queue2.append(p)
            s2 += p
            s1 -= p
            answer += 1
        elif s1 < s2:
            p = queue2.popleft()
            queue1.append(p)
            s1 += p
            s2 -= p
            answer += 1
        if p > s or answer >= 4*l:
            return -1
    return answer        