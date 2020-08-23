# https://www.acmicpc.net/problem/2583
# 영역 구하기
dx = [0,1,0,-1]
dy = [-1,0,1,0]
from collections import deque
if __name__ == '__main__':
    m,n,k = map(int,input().split())
    arr = [[1]*n for _ in range(m)]
    q = deque()
    area = 0
    cnt = []
    for i in range(k):
        x1,y1,x2,y2 = map(int,input().split())
        for y in range(m-y2,m-y1):
            for x in range(x1,x2):
                arr[y][x] = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                area += 1
                q.append((j,i))
                arr[i][j] = 0
                temp = 1
                while q:
                    now = q.popleft()
                    for l in range(4):
                        x = now[0] + dx[l]
                        y = now[1] + dy[l]
                        if 0 <= x < n and 0 <= y < m and arr[y][x] == 1:
                            arr[y][x] = 0
                            q.append((x,y))
                            temp += 1
                cnt.append(temp)
    print(area)
    cnt.sort()
    print(' '.join(map(str,cnt)))  
