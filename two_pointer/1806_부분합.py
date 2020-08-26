# https://www.acmicpc.net/problem/1806
# 

import sys
if __name__ == "__main__":
    n,s = map(int,sys.stdin.readline().split())
    arr = list(map(int,sys.stdin.readline().split()))
    l = r = 0
    total = counts = 0
    result = n+1
    while True:
        if total >= s:
            result = min(result,counts)
            total -= arr[l]
            counts -= 1
            l += 1
        else:
            if r == n:
                break
            total += arr[r]
            counts += 1
            r += 1
    if result != n+1:
        print(result)
    else:
        print(0)
