# https://www.acmicpc.net/problem/11403
# 경로찾기 --> 플로이드와샬 기본

import sys
if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    graph = [list(map(int,read().split())) for _ in range(n)]
    result = [i.copy() for i in graph] # 가중치 없어 경로가 있으면 가중치를 1로 지정
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if result[i][j] == 0:
                    temp = result[i][k]+result[k][j] 
                    temp = 1 if temp > 1 else 0 # 가중치가 1 이상이면 경로가 있다고 
                    result[i][j] = temp
    for i in result:
        print(' '.join(map(str,i)))
