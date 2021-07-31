# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 31                             | #
# | 2292 벌집                          | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    if N == 1:
        print(N)
        sys.exit()
    
    level = 2
    start_number = 2

    while True:
        end_number = start_number + 6 * (level - 1)

        if start_number <= N < end_number:
            print(level)
            break

        level += 1
        start_number = end_number
