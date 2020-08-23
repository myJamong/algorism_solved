# https://www.acmicpc.net/problem/15650
# 조합 구하기
'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.

입력
4 2

출력
1 2
1 3
1 4
2 3
2 4
3 4
'''
def dfs(l,s):
    if l == m:
        print(' '.join(map(str,arr)))
    else:
        for i in range(s,n):
            arr.append(i+1)
            dfs(l+1,i+1) # for문으로 탑색시 시작 노드의 수가 i+1인것이 
            arr.pop()

if __name__ == "__main__":
    n,m = map(int,input().split())
    arr = []
    dfs(0,0)
