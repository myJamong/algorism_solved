# https://www.acmicpc.net/problem/15656
# 중복 있는 수열
'''
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.
- N개의 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.

입력
4 2
9 8 7 1

출력 
1 1
1 7
1 8
1 9
7 1
7 7
7 8
7 9
8 1
8 7
8 8
8 9
9 1
9 7
9 8
9 9
'''
def dfs(l):
    if l == m:
        print(' '.join(map(str,res)))
    else:
        for i in range(n):
            res.append(arr[i])
            dfs(l+1)
            res.pop()

if __name__ == "__main__":
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    res = []
    dfs(0)
