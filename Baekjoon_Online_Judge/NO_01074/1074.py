# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 03                           | #
# | Day 08                             | #
# | 1074 Z                             | #
# -------------------------------------- #


def divide(start_row, start_col, length, number):
    end_row = start_row + length
    end_col = start_col + length

    if start_row <= r < end_row and start_col <= c < end_col:
        if length == 1:
            print(number)
            sys.exit()

        next_length = length // 2

        divide(start_row, start_col, next_length, number)
        divide(start_row, start_col + next_length, next_length, number + next_length ** 2)
        divide(start_row + next_length, start_col, next_length, number + next_length ** 2 * 2)
        divide(start_row + next_length, start_col + next_length, next_length, number + next_length ** 2 * 3)


if __name__ == "__main__":
    N, r, c = map(int, r_input().split())

    divide(0, 0, 2 ** N, 0)
