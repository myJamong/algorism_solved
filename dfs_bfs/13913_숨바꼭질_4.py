# https://www.acmicpc.net/problem/13913
# 숨바꼭질 4

import sys
from collections import deque
if __name__ == "__main__":
    a,b = map(int,sys.stdin.readline().split())
    if a <= b:
        chk = [0] * (100001)
        q = deque()
        q.append((a,0,str(a)))
        chk[a] = 1
        while q:
            now,time,res = q.popleft()
            if now == b:
                print(time)
                print(res)
                break
            nxt1,nxt2,nxt3 = now * 2, now + 1, now - 1
            temp = [nxt1,nxt2,nxt3]
            for nxt in temp:
                if 0 <= nxt <= 10**5 and chk[nxt] == 0:
                    q.append((nxt,time+1,res + ' {}'.format(nxt)))
                    chk[nxt] = 1
    else: # a가 더 큰 경우 하나씩 차감해서 들어가는 방법으로 해야 시간,메모리 초과를 피할 수 있다.
        print(a-b)
        for i in range(a,b-1,-1):
            print(i,end=' ')
