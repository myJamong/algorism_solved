# https://www.acmicpc.net/problem/16916
# 부분 문자열 --> KMP 기본 문제 패턴이 문자열 내부에 존재하는지 여부 확인

import sys
def make_pi(p):
    p_size = len(p)
    table = [0] * p_size
    j = 0
    for i in range(1,p_size):
        while j > 0 and p[i] != p[j]:
            j = table[j-1]
        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table

def kmp(S,P):
    s_size,p_size = len(S),len(P)
    table = make_pi(P)
    j = 0
    for i in range(s_size):
        while j > 0 and S[i] != P[j]:
            j = table[j-1]
        if S[i] == P[j]:
            if j == p_size - 1:
                return 1
            else:
                j += 1
    return 0

if __name__ == "__main__":
    read = sys.stdin.readline
    S = read().strip()
    P = read().strip()
    print(kmp(S,P))
