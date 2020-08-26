# https://www.acmicpc.net/problem/2512
# 예산

import sys
def max_budget(s):
    total = 0
    for i in arr:
        if i > s:
            total += s
        else:
            total += i
    return total

def binary(m,l,r):
    global result
    if l > r:
        return
    mid = (l + r) // 2
    if max_budget(mid) <= m:
        result = mid
        binary(m,mid+1,r)
    else:
        binary(m,l,mid-1)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))
    arr.sort()
    m = int(sys.stdin.readline())
    result = 0
    binary(m,0,max(arr))
    print(result)
