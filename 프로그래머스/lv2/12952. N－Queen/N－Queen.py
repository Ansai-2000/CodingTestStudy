def solution(n):
    queen = [0 for _ in range(n)]
    return dfs(queen,n,0)

def dfs(queen,n,row):
    count = 0
    if n == row:
        return 1
    for i in range(n):
        queen[row] = i
        
        for j in range(row):
            if queen[j] == queen[row]:
                break
            if abs(queen[j]-queen[row]) == row-j:
                break
        else:
            count += dfs(queen,n,row+1)
    return count        