# https://www.acmicpc.net/problem/10799
# 

import sys
if __name__ == "__main__":
    txt = sys.stdin.readline().strip()
    stack = []
    result = 0
    for i in range(len(txt)):
        c = txt[i]
        if c == '(':
            stack.append(c)
        else:
            stack.pop()
            if txt[i-1] == ')':
                result += 1
            else:
                result += len(stack)
    print(result)
