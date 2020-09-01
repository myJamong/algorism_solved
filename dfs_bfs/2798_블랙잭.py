# https://www.acmicpc.net/problem/2798
# 블랙잭

import sys
def dfs(l,total):
    global result
    if total > m:
        return
    if l == 3:
        if result < total <= m:
            result = total
    else:
        for i in range(len(arr)):
            if chk[i] == 0: # 같은 카드는 사용할 수 없기 때문에 분기에서 
                chk[i] = 1
                dfs(l+1,total+arr[i])
                chk[i] = 0

if __name__ == "__main__":
    read = sys.stdin.readline
    n,m = map(int,read().split())
    arr = list(map(int,read().split()))
    chk = [0] * n
    result = 0
    dfs(0,0)
    print(result)
