# https://www.acmicpc.net/problem/1874
# 스택 수열
import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    stack = []
    cnt = 0
    result = []
    for i in range(n):
        num = int(sys.stdin.readline())
        while True:
            if stack and stack[-1] == num:
                stack.pop()
                result.append('-')
                break
            else:
                if cnt > n:
                    break
                cnt += 1
                stack.append(cnt)
                result.append('+')
    if stack:
        print('NO')
    else:
        print('\n'.join(result))
