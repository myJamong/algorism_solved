# https://www.acmicpc.net/problem/6549
# 히스토그램에서 가장 큰 직사각형

import sys
if __name__ == "__main__":
    while True:
        n, *arr = list(map(int,sys.stdin.readline().split()))
        if n == 0:
            break
        arr.append(0)
        stack = []
        result = 0
        for idx,value in enumerate(arr):
            while stack:
                if stack[-1][1] > value:
                    i,h = stack.pop()
                    if stack:
                        # 스택에 있는 블럭이 붙어있지 않을 수 있기 때문에 거리는 스택의 -1값으로 해결해야함
                        temp = (idx - stack[-1][0] - 1) * h
                    else:
                        temp = idx * h
                    result = max(result,temp)
                else:
                    break
            stack.append((idx,value))
        print(result)
