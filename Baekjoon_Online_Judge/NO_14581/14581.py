# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 03                           | #
# | Day 02                             | #
# | 14581 팬들에게 둘러싸인 홍준        | #
# -------------------------------------- #


if __name__ == "__main__":
    my_id = r_input().rstrip()
    fan = ':fan:'

    print(fan * 3)
    print(fan + ':' + my_id + ':' + fan)
    print(fan * 3)
