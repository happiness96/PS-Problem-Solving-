# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 05                             | #
# | 17362 수학은 체육과목 입니다 2       | #
# -------------------------------------- #


if __name__ == "__main__":
    n = int(r_input()) - 1

    n %= 8

    print([1, 2, 3, 4, 5, 4, 3, 2][n])
