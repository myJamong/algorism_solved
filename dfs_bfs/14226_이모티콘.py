# https://www.acmicpc.net/problem/14226
# 이모티콘

import sys
from collections import deque
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    chk = [[0] * (1001) for _ in range(1001)]
    q = deque()
    q.append((1,0,0)) # 화면 출력 수, 클립보드, 시간
    while q:
        cnt, clip, time = q.popleft()
        if n == cnt:
            print(time)
            break
        if chk[cnt][clip] == 0: # 화면 출력과 클립보드의 이모티코 수가 같으면 다시 방문할 필요 없음
            chk[cnt][clip] = 1
            q.append((cnt,cnt,time+1))
            if clip != 0 and cnt + clip <= 1000: # 최소방법으로 해당 수를 넘어서 뒤로가는 방법도 있지만 밑에서 올라오는 방법도 동시에 존재
                q.append((cnt+clip,clip,time+1))
            if cnt-1 > 1:
                q.append((cnt-1,clip,time+1))
