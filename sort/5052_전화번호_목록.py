# https://www.acmicpc.net/problem/5052
# 전화번호 목록

import sys
if __name__ == "__main__":
    read = sys.stdin.readline
    T = int(read())
    for _ in range(T):
        n = int(read())
        book = []
        for _ in range(n):
            phone = read().strip()
            book.append(phone)
        book.sort()
        res = 'YES'
        for i in range(1,n):
            if book[i-1] == book[i][:len(book[i-1])]: # 정렬했을때 앞 번호전체가 뒤번호 첫번째 자리부터 전체가 일치할때
                res = 'NO'
                break
        print(res)
