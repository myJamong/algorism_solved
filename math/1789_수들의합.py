# https://www.acmicpc.net/problem/1789
# 수들의 합

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    result = 0
    for i in range(n):
        if i*(i+1)//2 <= n:
            result = i
            continue
        else:
            break
    print(result)
