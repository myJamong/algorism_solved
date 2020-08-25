# https://www.acmicpc.net/problem/9935
# 문자열 

import sys
if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    blow = sys.stdin.readline().strip()
    stack = []
    for c in line+' ':
        if len(stack) >= len(blow):
            if ''.join(stack[-(len(blow)):]) == blow:
                for i in range(len(blow)):
                    stack.pop()
        stack.append(c)
    if stack[0] != ' ':
        print(''.join(stack).strip())
    else:
        print('FRULA')
