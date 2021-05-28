# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 05                           | #
# | Day 28                             | #
# | 4673 셀프 넘버                      | #
# -------------------------------------- #


if __name__ == "__main__":
    self_number = [1] * 10001

    for number in range(1, 10001):
        str_number = str(number)

        total = number

        for n in str_number:
            total += int(n)
        
        if total < 10001:
            self_number[total] = 0
        
    for number in range(1, 10001):
        if self_number[number]:
            print(number)
