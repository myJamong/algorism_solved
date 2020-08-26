# https://www.acmicpc.net/problem/2748
# 피보나치 수2

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = [0] * (n+1)
    arr[1] = 1
    for i in range(2,n+1):
        arr[i] = arr[i-2] + arr[i-1]
    print(arr[n])
