# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 05                             | #
# | 9657 돌 게임 3                      | #
# -------------------------------------- #


if __name__ == "__main__":
    dp = [0] * 1001

    dp[1] = 1
    dp[3] = 1
    dp[4] = 1

    for ind in range(5, 1001):
        dp[ind] = not(dp[ind - 1] and dp[ind - 3] and dp[ind - 4])
    
    N = int(r_input())
    print(['CY', 'SK'][dp[N]])
