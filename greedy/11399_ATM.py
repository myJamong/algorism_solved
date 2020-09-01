# https://www.acmicpc.net/problem/11399
# ATM

import sys
if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    arr = list(map(int,read().split()))
    arr.sort()
    result = 0
    inc = 0
    for i in arr:
        inc += i
        result += inc
    print(result)
