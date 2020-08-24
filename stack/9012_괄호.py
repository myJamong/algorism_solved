# https://www.acmicpc.net/problem/9012
# 괄호
import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    for _ in range(n):
        stack = []
        line = sys.stdin.readline().strip()
        for c in line:
            if c == '(':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    print('NO')
                    break
        else:
            if stack:
                print('NO')
            else:
                print('YES')
