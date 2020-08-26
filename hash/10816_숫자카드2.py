# https://www.acmicpc.net/problem/10816
# 숫자카드2

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))
    arr.sort()
    m = int(sys.stdin.readline())
    finds = list(map(int,sys.stdin.readline().split()))
    dicts = {}
    for i in arr:
        if i in dicts:
            dicts[i] += 1
        else:
            dicts[i] = 1
    for i in finds:
        if i in dicts:
            print(dicts[i],end=' ')
        else:
            print(0,end=' ')
