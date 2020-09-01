# https://www.acmicpc.net/problem/1436
# 영화감독 숌

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    cnt = 666
    while n > 0:
        if '666' in str(cnt):
            n -= 1
        cnt += 1
    print(cnt-1)
