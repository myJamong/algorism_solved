# https://claude-u.tistory.com/258
# 순서 지켜야하고 동쪽중 서쪽의 갯수를 선택하는 것이므로 조합으로 해결 

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        l,r = map(int,input().split())
        answer = 1
        for i in range(r,r-l,-1):
            answer *= i
        for i in range(1,l+1):
            answer //= i
        print(answer)    
