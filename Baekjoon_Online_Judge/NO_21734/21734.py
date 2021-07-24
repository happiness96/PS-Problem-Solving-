# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 24                             | #
# | 21734 SMUPC의 등장                 | #
# -------------------------------------- #


if __name__ == "__main__":
    s = r_input().rstrip()

    for alpha in s:
        asc = ord(alpha)

        total = 0

        for val in str(asc):
            total += int(val)
        
        print(alpha * total)
