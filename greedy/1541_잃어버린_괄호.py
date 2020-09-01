# https://www.acmicpc.net/problem/1541
# 잃어버린 괄호

import sys
if __name__ == "__main__":
    arr = sys.stdin.readline().strip().split('-')
    result = sum(map(int,arr[0].split('+')))
    if len(arr) > 1:
        for i in range(1,len(arr)):
            result -= sum(map(int,arr[i].split('+')))
    print(result)
