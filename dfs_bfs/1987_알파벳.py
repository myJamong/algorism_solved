# https://www.acmicpc.net/problem/1987
# 알파벳
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    global result
    q = set()
    q.add((x,y,arr[y][x]))
    
    while q:
        now = q.pop()

        for i in range(4):
            xx = now[0] + dx[i]
            yy = now[1] + dy[i]

            if ((0 <= xx < c) and (0 <= yy < r)) and (arr[yy][xx] not in now[2]):
                q.add((xx,yy,now[2] + arr[yy][xx]))
                result = max(result, len(now[2])+1)

if __name__ == "__main__":
    r, c = map(int, input().split())
    arr = [list(input().strip()) for _ in range(r)]
    result = 1
    bfs(0,0)
    print(result)
