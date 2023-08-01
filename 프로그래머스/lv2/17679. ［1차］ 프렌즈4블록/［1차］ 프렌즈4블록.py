def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    while True:
        filter = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                a = board[i][j]
                b = board[i][j+1]
                c = board[i+1][j]
                d = board[i+1][j+1]
                if a == b == c == d != 0:
                    filter[i][j] = 1
                    filter[i][j+1] =1
                    filter[i+1][j] = 1
                    filter[i+1][j+1] = 1
        cnt = 0            
        for i in range(m):
            for j in range(n):
                if filter[i][j] == 1:
                    cnt+=1
                    board[i][j] = 0
        if cnt == 0:
            break
        answer += cnt 
        for i in range(m - 1, 0, -1):
            for j in range(n):
                if board[i][j] == 0:  
                    for k in range(i - 1, -1, -1):
                        if board[k][j] != 0: 
                            board[i][j] = board[k][j]
                            board[k][j] = 0
                            break      
    return answer