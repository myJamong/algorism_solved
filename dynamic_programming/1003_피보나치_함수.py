# https://www.acmicpc.net/problem/1003
# 피보나치 함수

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    for _ in range(n):
        num = int(sys.stdin.readline())    
        arr = [(0,0)] * (num+2)
        arr[0] = (1,0)
        arr[1] = (0,1)
        if num < 2:
            print(' '.join(map(str,arr[num])))
            continue
        for i in range(2,num+1):
            arr[i] = (arr[i-1][0]+arr[i-2][0],arr[i-1][1]+arr[i-2][1])
        print(' '.join(map(str,arr[num])))
