from collections import deque
def solution(board):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(len(board)):
        board[i] = list(board[i])
        if 'R' in board[i]:
            s = [i,board[i].index('R')]
    visited = [[0 for _ in range(len(board[0]))] for i in range(len(board))]  
    queue = deque([s]) 
    visited[s[0]][s[1]] = 1
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            while 0<=nx<len(board[0]) and 0<=ny<len(board):
                if board[ny][nx] == 'D':
                    break
                nx += dx[i]
                ny += dy[i]
            nx -= dx[i]
            ny -= dy[i]
            if board[ny][nx] == 'G':
                return visited[y][x]
            if visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny,nx])
    return -1   
  