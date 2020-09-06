# https://www.acmicpc.net/problem/1697
# 숨바꼭질

import sys
from collections import deque
if __name__ == "__main__":
    a,b = map(int,sys.stdin.readline().split())
    chk = [0] * (100001)
    q = deque()
    q.append((a,0))
    chk[a] = 1
    while q:
        now,time = q.popleft()
        if now == b:
            print(time)
            break
        nxt1,nxt2,nxt3 = now * 2, now + 1, now - 1
        temp = [nxt1,nxt2,nxt3]
        for nxt in temp:
            if 0 <= nxt <= 10**5 and chk[nxt] == 0: # 넓이 우선 탐색하는데 이미 방문한 가지는 안 뻗도록 막아줘야한다. 방문확인 필요
                q.append((nxt,time+1))        
                chk[nxt] = 1
