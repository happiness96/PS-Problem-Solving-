# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 26                             | #
# | 21738 얼음깨기 펭귄                 | #
# -------------------------------------- #


if __name__ == "__main__":
    N, S, P = map(int, r_input().split())

    for _ in range(N - 1):
        A, B = map(int, r_input().split())

