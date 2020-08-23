# https://www.acmicpc.net/problem/15663
# 배열에 같은 숫자가 존재하는 경우의 수열
'''
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
- N개의 자연수 중에서 M개를 고른 수열

입력
4 2
9 7 9 1

출력 
1 7
1 9
7 1
7 9
9 1
9 7
9 9
'''
def dfs(l):
    if l == m:
        print(' '.join(map(str,res)))
    else:
        before = 0 # 정렬된 배열에서 이전 숫자를 기억하여 비교한다.
        for i in range(n):
            if chk[i] == 0 and before != arr[i]:
                chk[i] = 1
                res.append(arr[i])
                before = arr[i]
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
