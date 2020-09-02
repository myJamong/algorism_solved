# https://www.acmicpc.net/problem/7562
# 나이트의 이동

import sys
from collections import deque
if __name__ == "__main__":
    dh = [-2,-2,-1,1,2,2,1,-1] # 11,1,2,4,5,7,8,10 시 방향 순서
    dw = [-1,1,2,2,1,-1,-2,-2]
    read = sys.stdin.readline
    T = int(read())
    for _ in range(T):
        n = int(read())
        arr = [[0]*n for _ in range(n)]
        h,w = map(int,read().split())
        y,x = map(int,read().split())
        q = deque()
        q.append((h,w))
        while q:
            now = q.popleft()
            if now[0] == y and now[1] == x: # 나이트 도달 위치 방문하면 빠져나오기 --> 시간 초과 해결
                break
            for d in range(8):
                hh = now[0] + dh[d]
                ww = now[1] + dw[d]
                if 0 <= hh < n and 0 <= ww < n and arr[hh][ww] == 0:
                    q.append((hh,ww))
                    arr[hh][ww] = arr[now[0]][now[1]] + 1
        print(arr[y][x])
