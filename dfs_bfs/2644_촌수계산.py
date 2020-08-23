# https://www.acmicpc.net/problem/2644
# 촌수 계산

from collections import deque
if __name__ == "__main__":
    node = int(input())
    p1,p2 = map(int,input().split())
    m = int(input())
    arr = [[0]*node for _ in range(node)]
    chk = [-1]*node
    for i in range(m):
        p,c = map(int,input().split())
        arr[p-1][c-1] = 1
        arr[c-1][p-1] = 1
        
    q = deque()
    q.append(p1-1)
    chk[p1-1] = 0
    while q:
        now = q.popleft()
        if now == p2-1:
            result = chk[now]
            break
        for i in range(node):
            if arr[now][i] == 1 and chk[i] == -1:
                chk[i] = chk[now] + 1
                q.append(i)
    print(chk[p2-1]) 
