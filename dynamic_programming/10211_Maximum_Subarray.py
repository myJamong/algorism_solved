# https://www.acmicpc.net/problem/10211
# Coder's High 2014 예비소집
# https://www.acmicpc.net/contest/view/41
import sys


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        max_sum = -float('inf')
        current_max_sum = 0
        for i in range(n):
            current_max_sum = max(0, current_max_sum) + arr[i]
            max_sum = max(max_sum, current_max_sum)
        print(max_sum)
"""
배열안의 수를 더해가면서 해당 위치의 최대값을 저장한다.
이때 부분집합의 합이 음수가 되는 순간... 그 이후는 어떤 수를 더하든 부분집합이 최대값이 절대 될 수 없다.
즉, 합이 음수가 되는 순간 초기화하고 새롭게 더해나가면서 기존의 최대값과 비교하는 것이 중요하다.
이렇게 하면 시간 복잡도가 O(N)
"""
