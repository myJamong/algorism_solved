# https://www.acmicpc.net/problem/15654
# 중복 없는 수열
'''
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.
-N개의 자연수 중에서 M개를 고른 수열

입력
4 2
9 8 7 1
'''
def dfs(l):
    if l == m:
        print(' '.join(map(str,res)))
    else:
        for i in range(n):
            if chk[i] == 0:
                chk[i] = 1
                res.append(arr[i])
                dfs(l+1)
                res.pop()
                chk[i] = 0

if __name__ == "__main__":
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    chk = [0] * n
    res = []
    dfs(0)
