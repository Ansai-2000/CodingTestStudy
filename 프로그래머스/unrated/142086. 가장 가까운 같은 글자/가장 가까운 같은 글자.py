def solution(s):
    answer = []
    arr = [-1]*26
    for i in range(len(s)):
        if(arr[ord(s[i])-ord('a')]==-1):
            answer.append(-1)
        else:
            answer.append(i-arr[ord(s[i])-ord('a')])
        arr[ord(s[i])-ord('a')] = i
    return answer