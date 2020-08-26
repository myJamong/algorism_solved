# https://www.acmicpc.net/problem/11726
# 2xn 타일링(Bottom-Up)

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = [0] * (n+2)
    arr[1] = 1
    arr[2] = 2
    for i in range(3,n+1):
        arr[i] = arr[i-2] + arr[i-1]
    print(arr[n] % 10007)
