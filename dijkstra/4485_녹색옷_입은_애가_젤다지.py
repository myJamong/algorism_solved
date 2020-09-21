# https://www.acmicpc.net/problem/4485
# 녹색옷 입은 애가 젤다지?

import sys
from heapq import heappop,heappush
if __name__ == "__main__":
    read = sys.stdin.readline
    cnt = 0
    dh = [-1,0,1,0]
    dw = [0,1,0,-1]
    while True:
        n = int(read())
        cnt += 1
        if n == 0:
            break
        board = [list(map(int,read().split())) for _ in range(n)]
        costs = [[sys.maxsize]*n for _ in range(n)]
        costs[0][0] = board[0][0]
        q = []
        heappush(q,(costs[0][0],0,0))
        while q:
            val,h,w = heappop(q)
            if h == n-1 and w == n-1:
                break
            for i in range(4):
                hh = h + dh[i]
                ww = w + dw[i]
                if 0 <= hh < n and 0 <= ww < n:
                    if costs[hh][ww] > val + board[hh][ww]: # 방문했는지 여부를 확인해서 진행해도 답 나옴
                        costs[hh][ww] = val + board[hh][ww]
                        heappush(q,(costs[hh][ww],hh,ww))
        print('Problem {}: {}'.format(cnt,costs[n-1][n-1]))        
