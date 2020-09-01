# https://www.acmicpc.net/problem/7568
# 덩치

import sys
if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    arr = [list(map(int,read().split())) for i in range(n)]
    for i in range(n):
        rank = 1        
        w,h = arr[i]
        for j in range(n):
            ww,hh = arr[j]
            if w < ww and h < hh:
                rank += 1
        print(rank,end=' ')
