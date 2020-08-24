# https://www.acmicpc.net/problem/10773
# 제로

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    stack = []
    for i in range(n):
        num = int(sys.stdin.readline())
        if num == 0:
            stack.pop()
        else:
            stack.append(num)
    print(sum(stack))
