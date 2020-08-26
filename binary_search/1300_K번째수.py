# https://www.acmicpc.net/problem/1300
# K번째 수

import sys
def counts(num):
    cnt = 0
    for i in range(1,n+1):
        cnt += min(num//i,n)
    return cnt

def binary(k,l,r):
    global result
    if l > r:
        return
    mid = (l+r) // 2
    if counts(mid) >= k:
        result = mid
        binary(k,l,mid-1)
    else:
        binary(k,mid+1,r)
    
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    result = 0
    binary(k,1,n**2)
    print(result)
