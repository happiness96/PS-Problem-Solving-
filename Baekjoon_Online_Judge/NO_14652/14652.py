# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 28                             | #
# | 14652 나는 행복합니다~              | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M, K = map(int, r_input().split())

    print(K // M, K % M)
