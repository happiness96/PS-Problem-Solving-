# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 06                             | #
# | 19563 개구리 1                     | #
# -------------------------------------- #


if __name__ == "__main__":
    a, b, c = map(int, r_input().split())
    distance = abs(a) + abs(b)

    if c >= distance and distance % 2 == c % 2:
        print('YES')
    
    else:
        print('NO')
