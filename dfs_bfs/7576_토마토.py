# https://www.acmicpc.net/problem/7576
# 토마토

import sys
from collections import deque
if __name__ == "__main__":
    dh = [-1,0,1,0] # 북, 동, 남, 서
    dw = [0,1,0,-1]
    read = sys.stdin.readline
    w,h = map(int,read().split())
    arr = [list(map(int,read().split())) for _ in range(h)]
    q = deque()
    for i in range(h): # 익어 있는 토마토 확인 후 데크에 삽입
        for j in range(w):
            if arr[i][j] == 1:
                q.append((i,j))
    while q:
        now = q.popleft() 먼저 들어간 좌표
        for d in range(4):
            hh = now[0] + dh[d]
            ww = now[1] + dw[d]
            if 0 <= hh < h and 0 <= ww < w and arr[hh][ww] == 0: # 상자 범위 안이고 안익은 토마토인 경우
                q.append((hh,ww)) # 큐에 삽입
                arr[hh][ww] = arr[now[0]][now[1]] + 1 # 이전 토마토 값보다 1 plus
    flag = True
    result = 0
    for i in range(h): # 안익은 토마토 있는지 확인
        for j in range(w):
            if arr[i][j] == 0:
                flag = False
                break
    if flag:
        for k in range(h):
            result = max(result,max(arr[k])) # 마지막 토마토 값 
    print(result-1)
