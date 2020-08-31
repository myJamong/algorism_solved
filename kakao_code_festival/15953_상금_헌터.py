# https://www.acmicpc.net/problem/15953
# 상금 헌터

import sys
if __name__ == "__main__":
    a_contest = [0,500,300,300,200,200,200,50,50,50,50,30,30,30,30,30,10,10,10,10,10,10]
    b_contest = [0,512,256,256,128,128,128,128,64,64,64,64,64,64,64,64]
    for i in range(16):
        b_contest.append(32)
    n = int(sys.stdin.readline())
    for _ in range(n):
        a,b = map(int,sys.stdin.readline().split())
        a_prize = b_prize = 0
        if 1 <= a <= 21:
            a_prize = a_contest[a]
        if 1 <= b <= 31:
            b_prize = b_contest[b]
        print((a_prize + b_prize)*10000)
