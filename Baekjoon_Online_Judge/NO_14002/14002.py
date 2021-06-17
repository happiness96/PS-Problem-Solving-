# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 17                             | #
# | 14002 가장 긴 증가하는 부분 수열 4  | #
# -------------------------------------- #


def run():
    N = int(r_input())
    A = list(map(int, r_input().split()))

    dp = [0] * 1001
    save = [0] * N

    for ind, val in enumerate(A):
        maximum = max(dp[:val]) + 1
        dp[val] = maximum
        save[ind] = maximum
    
    maximum = max(save)
    result = []

    print(maximum)

    for ind in range(N - 1,  -1, -1):
        if save[ind] == maximum:
            result.append(A[ind])
            maximum -= 1
    
    print(*result[::-1])


if __name__ == "__main__":
    run()
