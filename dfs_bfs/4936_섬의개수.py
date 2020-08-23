# https://www.acmicpc.net/problem/4963
# 섬의 개수

from collections import deque
dw = [0,1,1,1,0,-1,-1,-1]
dh = [-1,-1,0,1,1,1,0,-1]
if __name__ == "__main__":
    while True:
        w,h = map(int,input().split())
        if w == 0 and h == 0:
            break
        arr = [list(map(int,input().split())) for _ in range(h)]
        result = 0
        for i in range(h):
            for j in range(w):
                if arr[i][j] == 1:
                    arr[i][j] = 0
                    q = deque()
                    q.append((i,j))
                    while q:
                        now = q.popleft()
                        for k in range(8):
                            hh = now[0] + dh[k]
                            ww = now[1] + dw[k]
                            if 0 <= hh < h and 0 <= ww < w and arr[hh][ww] == 1:
                                arr[hh][ww] = 0
                                q.append((hh,ww))
                    result += 1
        print(result)
