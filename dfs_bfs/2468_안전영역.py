# https://www.acmicpc.net/problem/2468
# 안전 영역

from collections import deque
dx = [0,1,0,-1]
dy = [-1,0,1,0]
if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    q = deque()
    result = 0
                
    for h in range(0,101):
        chk = [[0]*n for _ in range(n)]
        temp = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j] > h and chk[i][j] == 0:
                    chk[i][j] = 1
                    q.append((i,j))
                    temp += 1
                    while q:
                        now = q.popleft()
                        for k in range(4):
                            x = now[0] + dx[k]
                            y = now[1] + dy[k]
                            if 0 <= x < n and 0 <= y < n and chk[x][y] == 0 and arr[x][y] > h:
                                chk[x][y] = 1
                                q.append((x,y))
        result = max(result, temp)
    print(result)
