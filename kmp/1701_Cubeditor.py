# https://www.acmicpc.net/problem/1701
# Cubeditor

import sys
def make_table(p):
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
    txt = sys.stdin.readline().strip()
    result = 0
    for i in range(len(txt)):
        s = txt[i:] # 시작 지점을 0번째부터 쭉 봤을때 pi table을 만드는 것 자체가 앞에서부터 뒤어서부터 동일한 문자열 --> 같은 문자열 2개인 길이를 배열로 반환
        table = make_table(s)
        result = max(result,max(table))
    print(result)
