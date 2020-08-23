# https://www.acmicpc.net/problem/1012
# 유기농 배추
# 문제에서 결국 구분된 영역의 갯수를 알아내면 그게 정답

from collections import deque
dw = [0,1,0,-1] # 가로 위치 변경용
dh = [-1,0,1,0] # 세로 위치 변경용
if __name__ == "__main__":
    T = int(input()) # 테스트 케이스 수
    for _ in range(T):
        w, h, k = map(int,input().split()) # 가로, 세로, 배추 수
        arr = [[0]*w for _ in range(h)] # 배추 영역
        result = 0 # 필요한 지렁이 마리 수
        
        # 배추 위치 입력
        for _ in range(k):
            x,y = map(int,input().split())
            arr[y][x] = 1
            
        # 각 영역 확인
        for i in range(h):
            for j in range(w):
                # 배추가 있는 경우
                if arr[i][j] == 1:
                    arr[i][j] = 0
                    q = deque()
                    q.append((i,j))
                    
                    # BFS 확인
                    while q:
                        now = q.popleft()
                        # 동서남북 4방향 확인
                        for l in range(4):
                            hh = now[0] + dh[l]
                            ww = now[1] + dw[l]
                            if 0 <= ww < w and 0 <= hh < h and arr[hh][ww] == 1:
                                arr[hh][ww] = 0
                                q.append((hh,ww))
                    result += 1
        print(result)
