def solution(N, road, K):
    answer = 0
    INF = 10e9
    graph = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(N+1):
        graph[i][i] = 0
    for s,e,v in road:
        graph[s][e] = min(graph[s][e],v)
        graph[e][s] = min(graph[e][s],v)
    for i in range(1,N+1):
        for j in range(1,N+1):
            for k in range(1,N+1):
                graph[j][k] = min(graph[j][i] + graph[k][i], graph[j][k])  
    return len([d for d in graph[1] if d<=K])
