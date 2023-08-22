def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for com in range(n):
        if visited[com] == False:
            dfs(n,computers,com,visited)
            answer+=1
    return answer

def dfs(n,computers,com,visited):
    visited[com] = True
    for i in range(n):
        if i != com and computers[com][i] == 1 and visited[i] == False:
            dfs(n,computers,i,visited)