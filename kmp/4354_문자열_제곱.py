# https://www.acmicpc.net/problem/4354
# 문자열 제곱

import sys
def make_pi(txt):
    size = len(txt)
    table = [0] * size
    j = 0
    for i in range(1,size):
        while j > 0 and txt[i] != txt[j]:
            j = table[j-1]
        if txt[i] == txt[j]:
            j += 1
            table[i] = j
    temp = size - table[-1] # 마지막에 숫자가 존재하는게 연속된 문자의 집합이라는 것을 알 수 있는 1차 방법
    n = size // temp # 제곱 수
    if txt[:temp]*n == txt: # 문쟈열 제곱 했을때 원 문자열과 같은지 확인
        return n
    return 1 # 아닌 경우 1 반환

if __name__ == "__main__":
    while True:
        txt = sys.stdin.readline().strip()
        if txt == '.':
            break
        print(make_pi(txt))
