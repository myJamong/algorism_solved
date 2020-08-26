# https://www.acmicpc.net/problem/2110
# 공유기 설치

import sys
def counts(dis):
    count = 1
    curr = arr[0]
    for i in range(1,len(arr)):
        if arr[i] - curr >= dis:
            count += 1
            curr = arr[i]
    return count

def binary(c,l,r):
    global result
    if l > r:
        return
    mid = (l + r) // 2
    if counts(mid) >= c:
        result = mid
        binary(c,mid+1,r)
    else:
        binary(c,l,mid-1)
    
if __name__ == "__main__":
    n,c = map(int,sys.stdin.readline().split())
    arr = [int(sys.stdin.readline()) for _ in range(n)]
    arr.sort()
    result = 0
    binary(c,arr[1]-arr[0],arr[-1]-arr[0])
    print(result)
