# https://www.acmicpc.net/problem/1305
# 광고

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
    
if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    txt = read().strip()
    print(n-make_pi(txt)[-1]) # 가장 긴 접두사와 접미사를 빼면 해결가능
