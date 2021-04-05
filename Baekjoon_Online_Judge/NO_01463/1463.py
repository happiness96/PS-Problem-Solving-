# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 05                             | #
# | 1463 1로 만들기                    | #
# -------------------------------------- #


def run():
    N = int(r_input())

    dp = [sys.maxsize] * (N + 1)
    dp[1] = 0

    for i in range(1, N):
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)

        if i * 2 <= N:
            dp[i * 2] = min(dp[i * 2] , dp[i] + 1)
        
        if i * 3 <= N:
            dp[i * 3] = min(dp[i * 3] , dp[i] + 1)
    
    print(dp[-1])


if __name__ == "__main__":
    run()
