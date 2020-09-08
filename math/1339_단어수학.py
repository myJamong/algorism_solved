# https://www.acmicpc.net/problem/1339
# 단어 수학

import sys
if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    chk = [0] * 26
    result = 0
    for _ in range(n):
        word = read().strip()
        for i in range(len(word)):
            chk[ord(word[i])-65] += 10**(len(word)-i-1) # 각 위치의 자리에 단어가 몇번 들어왔는지 확인
    chk.sort(reverse=True)
    start = 9
    for i in chk:
        if i != 0:
            result += i*start # 내림차순 정렬한 값에서 9부터 차례대로곱해주면 
            start -= 1
    print(result)
