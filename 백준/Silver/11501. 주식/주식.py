import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    answer = 0
    arr = list(map(int,input().split()))
    max = arr[-1]    
    for j in range(n-1,-1,-1):
        if max > arr[j]:
            answer += max - arr[j]
        else:
            max = arr[j]   
    print(answer)         
