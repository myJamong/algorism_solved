# https://www.acmicpc.net/problem/1786
# 찾기 --> kmp 기본

import sys
def make_table(P): # 찾는 패턴의 접두,접미 같은게 얼마나 있는지 배열로 나타내줌
    p_size = len(P)
    table = [0] * p_size
    j = 0
    for i in range(1,p_size):
        while j > 0 and P[i] != P[j]: # 접두가 같은 곳까지 빽
            j = table[j-1]
        if P[i] == P[j]:
            j += 1
            table[i] = j
    return table

def kmp(T,P):
    T_size = len(T)
    P_size = len(P)
    table = make_table(P)
    result = []
    j = 0
    for i in range(T_size):
        while j > 0 and T[i] != P[j]: # make_table의 방법과 비슷하게 찾는다.
            j = table[j-1]
        if T[i] == P[j]:
            if j == P_size-1:
                result.append(i-P_size+2)
                j = table[j]
            else:
                j += 1
    return result
                
if __name__ == "__main__":
    read = sys.stdin.readline
    T = read().rstrip()
    P = read().rstrip()
    arr = kmp(T,P)
    print(len(arr))
    for i in arr:
        print(i)
