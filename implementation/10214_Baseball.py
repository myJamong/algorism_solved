# https://www.acmicpc.net/problem/10214
# Coder's High 2014 예비소집
# https://www.acmicpc.net/contest/view/41

import sys

read = sys.stdin.readline

if __name__ == "__main__":
    T = int(read())
    for _ in range(T):
        Y, K = 0, 0
        for _ in range(9):
            a, b = map(int, read().split())
            Y += a
            K += b
        print('Yonsei' if Y > K else 'Korea' if Y < K else 'Draw')
"""
구현
비교하여 더한다.
"""
