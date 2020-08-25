# https://www.acmicpc.net/problem/1654
# 랜선 자르기

import sys
def count_lines(length):
    cnt = 0
    for line in arr:
        cnt += line//length
    return cnt

def binary(k,l,r):
    global result
    if l > r:
        return
    mid = (l+r) // 2
    if count_lines(mid) >= k:
        result = mid
        binary(k,mid+1,r)
    else:
        binary(k,l,mid-1)

if __name__ == "__main__":
    n,k = map(int,sys.stdin.readline().split())
    arr = [int(sys.stdin.readline()) for _ in range(n)]
    l,r = 1,max(arr)
    result = 0
    binary(k,l,r)
    print(result)
