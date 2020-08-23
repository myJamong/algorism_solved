# https://www.acmicpc.net/problem/15664
# 배열에 같은 숫자가 존재할 때 조합 구하기
'''
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
- N개의 자연수 중에서 M개를 고른 수열
- 고른 수열은 비내림차순이어야 한다.
  - 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
  
입력
4 2
9 7 9 1

출력 
1 7
1 9
7 9
9 9
'''
def dfs(l,s):
    if l == m:
        print(' '.join(map(str,res)))
    else:
        before = 0
        for i in range(s,n):
            if arr[i] != before:
                res.append(arr[i])
                before = arr[i]
                dfs(l+1,i+1)
                res.pop()
            
if __name__ == "__main__":
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    res = []
    dfs(0,0)
