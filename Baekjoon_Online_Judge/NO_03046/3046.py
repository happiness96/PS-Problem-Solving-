# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 12                             | #
# | 3046 R2                            | #
# -------------------------------------- #


if __name__ == "__main__":
    R1, S = map(int, r_input().split())

    R2 = S * 2 - R1

    print(R2)
