# https://www.acmicpc.net/problem/1463
# 1로 만들기(Bottom-Up) 

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = [0] * (n+3)
    arr[2] = 1
    arr[3] = 1
    for i in range(4,n+1):
        temp = []
        if i%2 == 0:
            temp.append(arr[i//2])
        if i%3 == 0:
            temp.append(arr[i//3])
        temp.append(arr[i-1])
        arr[i] = min(temp) + 1
    print(arr[n])
