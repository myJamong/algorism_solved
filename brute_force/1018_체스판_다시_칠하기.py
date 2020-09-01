# https://www.acmicpc.net/problem/1018
# 체스판 다시 칠하기

import sys
if __name__ == "__main__":
    a = [
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W']
    ]
    b = [
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
    ]
    read = sys.stdin.readline
    h,w = map(int,read().split())
    arr = [list(read().strip()) for _ in range(h)]
    result = 65
    for i in range(h-8+1):
        for j in range(w-8+1):
            for z in (a,b):
                cnt = 0
                for y in range(8):
                    for x in range(8):
                        if arr[i+y][j+x] != z[y][x]:
                            cnt += 1
                result = cnt if cnt < result else result
    print(result)
