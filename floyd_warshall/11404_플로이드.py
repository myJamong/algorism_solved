# https://www.acmicpc.net/problem/11404
# 플로이드

import sys
if __name__ == "__main__":
    read = sys.stdin.readline
    n  = int(read())
    m = int(read())
    INF = sys.maxsize
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,read().split())
        graph[a][b] = min(graph[a][b],c)
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] >= INF:
                graph[i][j] = 0
            if i == j:
                graph[i][j] = 0
    for i in graph[1:]:
        print(*i[1:])
