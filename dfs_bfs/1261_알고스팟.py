# https://www.acmicpc.net/problem/1261
# 알고스팟

import sys
from collections import deque
if __name__ == "__main__":
    dh,dw = [-1,0,1,0],[0,1,0,-1]
    read = sys.stdin.readline
    w,h = map(int,read().split())
    arr = [list(read().strip()) for _ in range(h)]
    chk = [[-1]*w for _ in range(h)]
    q = deque()
    q.append((0,0))
    chk[0][0] = 0
    while q:
        y,x = q.popleft()
        for k in range(4):
            hh,ww = y + dh[k],x + dw[k]
            if 0 <= hh < h and 0 <= ww < w:
                if chk[hh][ww] == -1:
                    if arr[hh][ww] == '1':
                        q.append((hh,ww))
                        chk[hh][ww] = chk[y][x] + 1
                    else:
                        q.appendleft((hh,ww)) # 가중치가 0인 경우 앞에 삽입 --> 최단 경로 찾기 위함
                        chk[hh][ww] = chk[y][x]
    print(chk[h-1][w-1])
