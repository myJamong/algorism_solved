# https://www.acmicpc.net/problem/1931
# 회의실 배정

import sys
if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    arr = [list(map(int,read().split())) for _ in range(n)]
    arr.sort(key=lambda x:(x[1],x[0])) # 끝나는 시간으로 오름차순 정렬 --> 두번째 키로 시작시간 정렬 필요. 22 12 순서로 들어오면 12 22 순으로 2개가 정답임
    key = arr[0][1]
    result = 1
    for i in range(1,len(arr)):
        start,end = arr[i]
        if start >= key:
            key = end
            result += 1
    print(result)
