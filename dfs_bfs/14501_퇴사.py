# https://www.acmicpc.net/problem/14501
# 퇴사

import sys
def dfs(day,total):
    global result
    if day == n:
        if total > result:
            result = total
    else:
        if day + arr[day][0] <= n:
            dfs(day+arr[day][0],total+arr[day][1])
        dfs(day+1,total)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    result = 0
    dfs(0,0)
    print(result)
