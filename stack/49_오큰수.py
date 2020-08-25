# https://suri78.tistory.com/49
# 오큰수

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))
    result = [-1] * n
    stack = [0]
    for i in range(1,n):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack[-1]] = arr[i]
            stack.pop()
        stack.append(i)
    print(' '.join(map(str,result)))
