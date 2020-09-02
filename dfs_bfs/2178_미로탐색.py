# https://www.acmicpc.net/problem/2178
# 미로탐색
 
import sys
from collections import deque
if __name__ == "__main__":
    dh = [-1,0,1,0]
    dw = [0,1,0,-1]
    read = sys.stdin.readline
    h,w = map(int,read().split())
    arr = [list(read().strip()) for _ in range(h)]
    q = deque()
    q.append((0,0)) # 0,0 시작
    while q:
        now = q.popleft()
        for d in range(4):
            hh = now[0] + dh[d]
            ww = now[1] + dw[d]
            if 0 <= hh < h and 0 <= ww < w and arr[hh][ww] == '1':
                q.append((hh,ww))
                arr[hh][ww] = int(arr[now[0]][now[1]]) + 1 # 이전 위치보다 +1
    print(arr[h-1][w-1]) # 우측하단 값 
