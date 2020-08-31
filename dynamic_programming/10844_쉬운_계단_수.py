# https://www.acmicpc.net/problem/10844
# 쉬운 계단 수

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    d = [0,1,1,1,1,1,1,1,1,1] # 숫자의 마지막 자리 수 갯수 0 ~ 9
    for i in range(n-1):
        temp = [0] * 10
        for j in range(10):
            if j == 0:
                temp[1] += d[j]
            elif j == 9:
                temp[8] += d[j]
            else:
                temp[j-1] += d[j]
                temp[j+1] += d[j]
        d = temp
    print(sum(d)%1000000000)
