# https://www.acmicpc.net/problem/1406
# 에디터

import sys
from collections import deque
if __name__ == "__main__":
    l_stack = list(sys.stdin.readline().strip())
    r_q = deque()
    n = int(sys.stdin.readline())
    for _ in range(n):
        orders = sys.stdin.readline().split()
        if orders[0] == 'L' and l_stack:
            r_q.appendleft(l_stack.pop())
        elif orders[0] == 'D' and r_q:
            l_stack.append(r_q.popleft())
        elif orders[0] == 'B' and l_stack:
            l_stack.pop()
        elif orders[0] == 'P':
            l_stack.append(orders[1])
    print(''.join(l_stack + list(r_q)))
