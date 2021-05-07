# -*- encoding: utf-8 -*-
import sys
from itertools import combinations
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 05                           | #
# | Day 07                             | #
# | 21312 홀짝 칵테일                   | #
# -------------------------------------- #


if __name__ == "__main__":
    A, B, C = map(int, r_input().split())

    odd = []
    even = []

    for case in (A, B, C, A * B, B * C, A * C, A * B * C):
        if case % 2:
            odd.append(case)
        
        else:
            even.append(case)
    
    if odd:
        print(max(odd))
    
    else:
        print(max(even))
