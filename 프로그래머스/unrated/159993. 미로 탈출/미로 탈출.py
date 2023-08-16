from collections import deque
def solution(maps):
    answer = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(len(maps)):
        maps[i] = list(maps[i])
    for i in range(len(maps)):
        if 'S' in maps[i]:
            s = [i,maps[i].index('S')]
    queue = deque([s])
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[s[0]][s[1]] = 1
    flag = False
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<len(maps[0]) and 0<=ny<len(maps) and visited[ny][nx] == 0 and maps[ny][nx] != "X":
                if maps[ny][nx] == "O" or maps[ny][nx] == 'E':
                    queue.append([ny,nx])
                    visited[ny][nx] = visited[y][x] + 1
                elif maps[ny][nx] == "L":
                    visited[ny][nx] = visited[y][x] + 1
                    s = ny,nx
                    flag = True
                    answer = visited[ny][nx] -1
    if flag == False:
        return -1
    queue = deque([s])  
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[s[0]][s[1]] = 1
    flag = False
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<len(maps[0]) and 0<=ny<len(maps) and visited[ny][nx] == 0 and maps[ny][nx] != "X":
                if maps[ny][nx] == "O" or maps[ny][nx] == 'S':
                    queue.append([ny,nx])
                    visited[ny][nx] = visited[y][x] + 1
                elif maps[ny][nx] == "E":
                    visited[ny][nx] = visited[y][x] + 1
                    flag = True
                    answer += visited[ny][nx] -1
    if flag == False:
        return -1
    return answer
