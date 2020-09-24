# https://www.acmicpc.net/problem/9205
# 맥주마시면서 걸어가기 --> 플로이드와샬로 풀면 pypy로 제출해야함 --> 플로이드와샬은 꼭 필요할때만 쓰자. 왼만하면 DFS나 BFS로 풀려고해 오래걸려

#플로이드 와샬
import sys
def distance(loc1,loc2):
    return abs(loc1[0]-loc2[0]) + abs(loc1[1]-loc2[1])

if __name__ == "__main__":
    read = sys.stdin.readline
    T = int(read())
    INF = sys.maxsize
    for _ in range(T):
        n = int(read())
        loc = []
        for _ in range(n+2):
            a,b = map(int,read().split())
            loc.append((a,b))
        graph = [[INF]*(n+2) for _ in range(n+2)]
        for i in range(n+2):
            for j in range(i,n+2):
                temp = distance(loc[i],loc[j])
                if temp <= 1000:
                    graph[i][j] = temp
                    graph[j][i] = temp
                if i == j:
                    graph[i][j] = 0
        for k in range(n+2):
            for i in range(n+2):
                for j in range(n+2):
                    graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
        print('happy' if graph[0][-1] != INF else 'sad')
        
# BFS
import sys
from collections import deque
def distance(loc1,loc2):
    return abs(loc1[0]-loc2[0]) + abs(loc1[1]-loc2[1])

if __name__ == "__main__":
    read = sys.stdin.readline
    T = int(read())
    INF = sys.maxsize
    for _ in range(T):
        n = int(read())
        loc = []
        for _ in range(n+2):
            a,b = map(int,read().split())
            loc.append((a,b))
        graph = [[0]*(n+2) for _ in range(n+2)]
        for i in range(n+2):
            for j in range(i,n+2):
                temp = distance(loc[i],loc[j])
                if temp <= 1000:
                    graph[i][j] = temp
                    graph[j][i] = temp
        q = deque()
        q.append(0)
        visit = [0] * (n+2)
        visit[0] = 1
        res = 'sad'
        while q:
            now = q.popleft()
            if now == n+2-1:
                res = 'happy'
            for i in range(n+2):
                if visit[i] == 0 and graph[now][i] > 0:
                    visit[i] = 1
                    q.append(i)
        print(res)
