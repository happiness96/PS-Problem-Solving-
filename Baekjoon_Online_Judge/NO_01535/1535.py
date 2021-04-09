# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 08                             | #
# | 1535 안녕                          | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    L = list(map(int, r_input().split()))
    J = list(map(int, r_input().split()))

    health = [0] * 101
    
    for ind in range(N):
        for rem, val in enumerate(health):
            if rem > L[ind]:
                health[rem - L[ind]] = max(health[rem - L[ind]], health[rem] + J[ind])
    
    print(max(health))
