# https://www.acmicpc.net/problem/7569
# 토마토 --> 3차원 형식의 BFS

import sys
from collections import deque

def solve():
    dn = [-1,0,1,0,0,0] # 북, 동, 남, 서, 상, 하
    dm = [0,1,0,-1,0,0]
    dh = [0,0,0,0,-1,1]
    read = sys.stdin.readline
    m,n,h = map(int,read().split())
    arr = [[list(map(int,read().split())) for _ in range(n)] for _ in range(h)]
    q = deque()
    result = 0
    cnt = 0
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if arr[z][y][x] == 0:
                    cnt += 1 # 총 없애야할 안익은 토마토 수
                if arr[z][y][x] == 1:
                    q.append((z,y,x,0))
    while q and cnt:
        for _ in range(len(q)):
            now = q.popleft()
            result = max(result,now[3])
            for i in range(6):
                zz = now[0]+dh[i]
                yy = now[1]+dn[i]
                xx = now[2]+dm[i]
                if 0 <= zz < h and 0 <= yy < n and 0 <= xx < m and arr[zz][yy][xx] == 0:
                    arr[zz][yy][xx] = 1
                    q.append((zz,yy,xx,now[3]+1))
                    cnt -= 1
        result += 1
    print(result if cnt == 0 else -1) # 안익은 토마토가 남아있으면 -1
    
if __name__ == "__main__":
    solve()
