# https://www.acmicpc.net/problem/15655
# 중복없는 조합
'''
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.
- N개의 자연수 중에서 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.

입력
4 2
9 8 7 1

출력
1 7
1 8
1 9
7 8
7 9
8 9
'''
def dfs(l,s):
    if l == m:
        print(' '.join(map(str,res)))
    else:
        for i in range(s,n):
            res.append(arr[i])
            dfs(l+1,i+1)
            res.pop()
        
if __name__ == "__main__":
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    res = []
    dfs(0,0)
