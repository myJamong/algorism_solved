# https://www.acmicpc.net/problem/1065
# 한수

import sys
def hansu(n):
    num3 = n // 100
    num2 = (n % 100) // 10
    num1 = (n % 100) % 10
    if num3 - num2 == num2 - num1:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    cnt = 99
    if n < 100:
        print(n)
    else:
        for i in range(100,n+1):
            if hansu(i):
                cnt += 1
        print(cnt)
