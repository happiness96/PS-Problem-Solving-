# -*- encoding: utf-8 -*-
import sys
from itertools import combinations
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 26                             | #
# | 21968 선린의 터를                   | #
# -------------------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for _ in range(T):
        N = int(r_input())

        bin_N = bin(N)[2:]
        
        result = int(bin_N, 3)

        print(result)
