# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 17                             | #
# | 21313 문어                          | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    if N % 2:
        print('1 2 ' * (N // 2) + '3')
    
    else:
        print('1 2 ' * (N // 2))
