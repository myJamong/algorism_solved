# https://www.acmicpc.net/problem/2805
# 나무 

import sys
def cuts(h):
    length = 0
    for i in arr:
        if i > h:
            length += i - h
    return length

def binary(m,l,r):
    global result
    if l > r:
        return
    mid = (l+r) // 2
    if cuts(mid) >= m:
        result = mid
        binary(m,mid+1,r)
    else:
        binary(m,l,mid-1)

if __name__ == "__main__":
    n,m = map(int,sys.stdin.readline().split())
    arr = list(map(int,sys.stdin.readline().split()))
    l,r = 0,max(arr)
    result = 0
    binary(m,l,r)
    print(result)
