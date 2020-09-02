# https://www.acmicpc.net/problem/2667
# 단지번호붙이기

import sys
from collections import deque
if __name__ == "__main__":
    dh = [-1,0,1,0]
    dw = [0,1,0,-1]
    read = sys.stdin.readline
    n = int(read())
    arr = [list(read().strip()) for _ in range(n)]
    total = 0
    res = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '1': # 아파트 있는지 확인
                total += 1 # 단지 수 +1
                q = deque()
                q.append((i,j))
                arr[i][j] = '0' # 처음 확인한 값은 0 으로 --> 단지에 아파트가 1개일때 반례 --> 다시 확인하지 않게 하기 위해
                cnt = 0
                while q:
                    now = q.popleft()
                    cnt += 1
                    for d in range(4):
                        h = now[0] + dh[d]
                        w = now[1] + dw[d]
                        if 0 <= h < n and 0 <= w < n and arr[h][w] == '1': # 아파트인지 확인
                            arr[h][w] = '0'
                            q.append((h,w))
                res.append(cnt)
    res.sort()
    res.insert(0,total)
    print('\n'.join(map(str,res)))
