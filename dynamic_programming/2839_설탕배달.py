# https://www.acmicpc.net/problem/2839
# 설탕 배달(Bottom-Up)

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = [-1] * (n+5)
    arr[3] = arr[5] = 1
    for i in range(6,n+1):
        temp = []
        if arr[i-3] != -1:
            temp.append(arr[i-3])
        if arr[i-5] != -1:
            temp.append(arr[i-5])
        if temp:
            arr[i] = min(temp) + 1
    print(arr[n])
