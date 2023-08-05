def solution(arr):
    answer = [0,0]
    def div(a,b,n):
        s = arr[a][b]
        for i in range(a,a+n):
            for j in range(b,b+n):
                if arr[i][j] != s:
                    n = n//2
                    div(a,b,n)
                    div(a+n,b,n)
                    div(a,b+n,n)
                    div(a+n,b+n,n)
                    return
        answer[s] += 1        
    div(0,0,len(arr))
    return answer    