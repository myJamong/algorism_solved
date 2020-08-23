# https://www.acmicpc.net/problem/15652
# 중복 있는 조합
'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
- 1부터 N까지 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 고른 수열은 비내림차순이어야 한다.
  -길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

입력
4 2

출력
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4
'''
def dfs(l):
    if l == m:
        print(' '.join(map(str,arr)))
    else:
        for i in range(n):
            if arr:
                if arr[-1] <= i+1: # 오름차순으로 숫자가 들어온다고 가정했을 때 이전에 들오온 번호보다 같거나 큰 경우에만 가지를 뻗는다.
                    arr.append(i+1)
                    dfs(l+1)
                    arr.pop()
            else: # 처음 배열에 넣을 때는 모든 경우로 가지를 뻗는다.
                arr.append(i+1)
                dfs(l+1)
                arr.pop()

if __name__ == "__main__":
    n,m = map(int,input().split())
    arr = []
    dfs(0)
