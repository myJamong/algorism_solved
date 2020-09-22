# https://www.acmicpc.net/problem/11585
# 속타는 저녁 메뉴

import sys
import math
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
    size = int(read())
    txt = read().split()
    table = make_pi(txt)
    temp = size - table[-1] # 접두사 접미사 동일할때의 크기
    n = size // temp # 반복되는 문자라면 몇번 반복되는지
    if txt[:temp]*n == txt:
        gcd = math.gcd(n,size) # 최대 공약수 구하기
        print('{}/{}'.format(n//gcd,size//gcd))
    else:
        print('1/{}'.format(size))
