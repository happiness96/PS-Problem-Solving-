# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 03                           | #
# | Day 08                             | #
# | 1434 책 정리                        | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())
    A = list(map(int, r_input().split()))
    B = list(map(int, r_input().split()))

    print(sum(A) - sum(B))
