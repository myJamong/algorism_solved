# https://www.acmicpc.net/problem/2493
# 탑
import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))
    stack = []
    for idx,value in enumerate(arr,1):
        while True:
            if not stack:
                print(0,end=' ')
                stack.append((value,idx))
                break
            else:
                if stack[-1][0] < value:
                    stack.pop()
                else:
                    print(stack[-1][1],end=' ')
                    stack.append((value,idx))
                    break
