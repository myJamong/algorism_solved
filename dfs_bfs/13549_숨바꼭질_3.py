# https://www.acmicpc.net/problem/13549
# 숨바꼭질 3

import sys
from collections import deque
if __name__ == "__main__":
    a,b = map(int,sys.stdin.readline().split())
    if b >= a:
        chk = [0] * (100001)
        q = deque()
        q.append((a,0))
        chk[a] = 1
        while q:
            now,time = q.popleft()
            if now == b:
                print(time)
                break
            nxt1,nxt2,nxt3 = now*2,now+1,now-1
            temp = [nxt1,nxt2,nxt3]
            for i in range(3):
                t = temp[i]
                if 0 <= t <= 10**5 and chk[t] == 0:
                    if i == 0:
                        q.appendleft((t,time)) # 2를 곱했을때 우선순위를 줌 --> 최소비용이기 때문에 일단 2부터 끝가지 곱한다.
                    else:
                        q.append((t,time+1))
                    chk[temp[i]] = 1
    else:
        print(a-b)
