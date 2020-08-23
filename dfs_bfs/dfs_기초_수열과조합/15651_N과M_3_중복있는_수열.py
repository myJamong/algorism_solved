# https://www.acmicpc.net/problem/15651
# 중복 있는 수열
'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
- 1부터 N까지 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.

입력
4 2

출력
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4
'''
def dfs(l):
    if l == m:
        print(' '.join(map(str,arr)))
    else:
        for i in range(n):
            arr.append(i+1)
            dfs(l+1)
            arr.pop()

if __name__ == "__main__":
    n,m = map(int,input().split())
    arr = [] # 중복 없는 수열과 다르게 확인용 
    dfs(0)
