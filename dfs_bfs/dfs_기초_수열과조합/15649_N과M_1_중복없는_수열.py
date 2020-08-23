# https://www.acmicpc.net/problem/15649
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# - 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
'''
입력 
4 2

출력
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
'''
def dfs(l):
    if l == m:
        print(' '.join(map(str,arr)))
    else:
        for i in range(n):
            if chk[i] == 0:
                chk[i] = 1
                arr.append(i+1)
                dfs(l+1)
                arr.pop()
                chk[i] = 0

if __name__ == "__main__":
    n,m = map(int,input().split())
    arr = []
    chk = [0] * n # 확인용 배열을 통해 가지를 뻗어 나갈때 갈수 있는지 없는지를 확인 --> 중복 
    dfs(0)
