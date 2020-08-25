# https://www.acmicpc.net/problem/1935
# 후위표기식2

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    line = sys.stdin.readline().strip()
    stack = []
    nums = [int(sys.stdin.readline()) for _ in range(n)]
    for c in line:
        if 'A' <= c <= 'Z':
            stack.append(nums[ord(c)-ord('A')])
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if c == '*':
                stack.append(num2*num1)
            elif c == '/':
                stack.append(num2/num1)
            elif c == '+':
                stack.append(num2+num1)
            else:
                stack.append(num2-num1)
    print('%.2f' % stack.pop())
