# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 01                             | #
# | 19947 투자의 귀재 배주형            | #
# -------------------------------------- #


if __name__ == "__main__":
    H, Y = map(int, r_input().split())

    dp = [0] * (Y + 1)
    dp[0] = H

    for i in range(Y + 1):
        if i + 1 <= Y:
            dp[i + 1] = max(dp[i + 1], int(dp[i] * 1.05))
        
        if i + 3 <= Y:
            dp[i + 3] = max(dp[i + 3], int(dp[i] * 1.2))
        
        if i + 5 <= Y:
            dp[i + 5] = max(dp[i + 5], int(dp[i] * 1.35))
        
    print(max(dp))
