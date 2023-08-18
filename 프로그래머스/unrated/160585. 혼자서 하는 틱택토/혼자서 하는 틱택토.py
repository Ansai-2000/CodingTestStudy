def solution(board):
    answer = -1
    for i in range(len(board)):
        board[i] = list(board[i])
    ocnt = 0
    xcnt = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'O':
                ocnt += 1
            elif board[i][j] == 'X':
                xcnt += 1
    olcount = [tic1(board,0,0,'O',0) , tic1(board,1,0,'O',0) , tic1(board,2,0,'O',0) , tic2(board,0,0,'O',0) , tic2(board,0,1,'O',0) , tic2(board,0,2,'O',0) , tic3(board,0,0,'O',0) , tic4(board,0,2,'O',0)].count(True)
    xlcount = [tic1(board,0,0,'X',0) , tic1(board,1,0,'X',0) , tic1(board,2,0,'X',0) , tic2(board,0,0,'X',0) , tic2(board,0,1,'X',0) , tic2(board,0,2,'X',0) , tic3(board,0,0,'X',0) or tic4(board,0,2,'X',0)].count(True)
    if ocnt > xcnt + 1:
        return 0
    if xcnt > ocnt:
        return 0
    if olcount + xlcount > 1:
        if olcount == 2 and ocnt - xcnt == 1:
            return 1
        return 0
    if olcount == 1 and ocnt == xcnt:
        return 0
    if xlcount == 1 and ocnt > xcnt :
        return 0
    return 1
    
def tic1(board,y,x,o,n):
    if n==3:
        return True
    if y < 0 or y >= 3 or x < 0 or x >= 3:
        return False
    if board[y][x] == o:
        return tic1(board,y,x+1,o,n+1)
    else:
        return False
def tic2(board,y,x,o,n):
    if n==3:
        return True
    if y < 0 or y >= 3 or x < 0 or x >= 3:
        return False
    if board[y][x] == o:
        return tic2(board,y+1,x,o,n+1)
    else:
        return False
def tic3(board,y,x,o,n):
    if n==3:
        return True
    if y < 0 or y >= 3 or x < 0 or x >= 3:
        return False
    if board[y][x] == o:
        return tic3(board,y+1,x+1,o,n+1)
    else:
        return False   
def tic4(board,y,x,o,n):
    if n==3:
        return True
    if y < 0 or y >= 3 or x < 0 or x >= 3:
        return False
    if board[y][x] == o:
        return tic4(board,y+1,x-1,o,n+1)
    else:
        return False    