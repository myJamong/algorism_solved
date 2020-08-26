# https://www.acmicpc.net/problem/1932
# 정수 삼각형

import sys
        
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,sys.stdin.readline().split())))
    for i in range(1,n):
        for j in range(i+1):
            if j==0:
                arr[i][j] += arr[i-1][j]
            elif j == i:
                arr[i][j] += arr[i-1][j-1]
            else:
                arr[i][j] += max(arr[i-1][j],arr[i-1][j-1])
    print(max(arr[-1]))
