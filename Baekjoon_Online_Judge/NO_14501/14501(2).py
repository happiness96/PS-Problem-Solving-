# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 05                             | #
# | 14501 퇴사                          | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    consulting = [(0, 0)]
    dp = [0] * (N + 1)

    for _ in range(N):
        T, P = map(int, r_input().split())

        consulting.append((T, P))
    
    for ind, consult in enumerate(consulting):
        if not ind:
            continue

        T, P = consult

        if ind + T <= N + 1:
            dp[ind + T - 1] = max(dp[ind + T - 1], max(dp[: ind]) + P)
    
    print(max(dp))
