from collections import deque
def solution(maps):
    queue = deque()
    n = len(maps)
    m = len(maps[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue.append([0,0])
    while queue:
        a = queue.popleft()
        [x,y] = a
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx < 0 or xx >= n or yy < 0 or yy >= m:
                continue
            if maps[xx][yy] == 0:
                continue
            if maps[xx][yy] == 1 or maps[xx][yy] > maps[x][y] + 1:
                maps[xx][yy] = maps[x][y] + 1
                queue.append([xx,yy])
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1       