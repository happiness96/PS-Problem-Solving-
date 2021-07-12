# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 12                             | #
# | 16204 카드 뽑기                      | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M, K = map(int, r_input().split())

    print(min(M, K) + min(N - M, N - K))
