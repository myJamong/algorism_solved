# https://www.acmicpc.net/problem/15666
# 중복있는 조합 배열에 같은 숫자가 존재할 때
'''
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
- N개의 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 고른 수열은 비내림차순이어야 한다.
  - 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

입력
4 2
9 7 9 1

출력 
1 1
1 7
1 9
7 7
7 9
9 9
'''
def dfs(l):
    if l == m:
        print(' '.join(map(str,res)))
    else:
        before = 0
        res_before = 0
        for i in range(n):
            if res:
                res_before = res[-1]
            if arr[i] != before and arr[i] >= res_before:
                res.append(arr[i])
                before = arr[i]
                dfs(l+1)
                res.pop()

if __name__ == "__main__":
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    res = []
    dfs(0)
