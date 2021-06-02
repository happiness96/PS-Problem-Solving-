# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 02                             | #
# | 10164 격자상의 경로                 | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M, K = map(int, r_input().split())

    K_row, K_col = divmod(K - 1, M)

    if K == 0:
        K_row, K_col = 0, 0

    dp = [1] * (K_col + 1)

    for _ in range(K_row):
        for ind in range(1, K_col + 1):
            dp[ind] += dp[ind - 1]
    
    K_row, K_col = N - K_row - 1, M - K_col - 1

    dp = [dp[-1]] * (K_col + 1)

    for _ in range(K_row):
        for ind in range(1, K_col + 1):
            dp[ind] += dp[ind - 1]
    
    print(dp[-1])
