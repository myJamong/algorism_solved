# https://www.acmicpc.net/problem/1389
# 케빈 베이컨의 6단계 

import sys
if __name__ == "__main__":
    INF = sys.maxsize
    read = sys.stdin.readline
    n,m = map(int,read().split())
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,read().split())
        graph[a][b] = 1
        graph[b][a] = 1
    res = [i.copy() for i in graph]
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                res[i][j] = min(res[i][j],res[i][k]+res[k][j])
    result = INF
    r = 0
    for i in range(n,0,-1):
        temp = sum(res[i][1:])
        if temp <= result:
            result = temp
            r = i
    print(r)
