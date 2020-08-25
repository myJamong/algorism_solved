# https://www.acmicpc.net/problem/17608
# 막대기

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    stack = []
    for _ in range(n):
        num = int(sys.stdin.readline())
        if stack:
            while stack and stack[-1] <= num:
                stack.pop()
            stack.append(num)
        else:
            stack.append(num)
    print(len(stack))
