# https://www.acmicpc.net/problem/2504
# 괄호의 값

import sys
if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    stack = []
    for i in line:
        if i in '([':
            stack.append(i)
        elif i == ')':
            num = 0
            while stack:
                top = stack.pop()
                if top == '(':
                    if num == 0:
                        stack.append('2')
                    else:
                        stack.append(str(2*num))
                    break
                elif top.isdigit():
                    num += int(top)
                elif top == '[':
                    print(0)
                    exit(0)
        elif i == ']':
            num = 0
            while stack:
                top = stack.pop()
                if top == '[':
                    if num == 0:
                        stack.append('3')
                    else:
                        stack.append(str(3*num))
                    break
                elif top.isdigit():
                    num += int(top)
                elif top == '(':
                    print(0)
                    exit(0)
    for i in stack:
        if not i.isdigit():
            stack = []
    print(sum(map(int,stack)))
