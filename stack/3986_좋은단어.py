# https://www.acmicpc.net/problem/3986
# 좋은 단어
import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    cnt = 0
    for _ in range(n):
        line = sys.stdin.readline().strip()
        stack = []
        for i in line:
            if stack:
                if stack[-1] == i:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        if not stack:
            cnt += 1
    print(cnt)  
