# https://www.acmicpc.net/problem/1260
# DFS와 BFS

import sys
from collections import deque
def dfs(idx):
    print(idx,end=' ')
    chk[idx] = 1
    for i in range(1,n+1):
        if arr[idx][i] == 1 and chk[i] == 0:
            dfs(i)
    
def bfs(idx):
    q = deque()
    q.append(idx)
    chk[idx] = 0
    while q:
        now = q.popleft()
        print(now,end=' ')
        for i in range(1,n+1):
            if arr[now][i] == 1 and chk[i] == 1:
                q.append(i)
                chk[i] = 0
            
if __name__ == "__main__":
    read = input
    n,m,v = map(int,read().split())
    arr = [[0]*(n+1) for _ in range(n+1)]
    chk = [0] * (n+1)
    for _ in range(m):
        a,b = map(int,read().split())
        arr[a][b] = 1
        arr[b][a] = 1
    dfs(v)
    print()
    bfs(v)
