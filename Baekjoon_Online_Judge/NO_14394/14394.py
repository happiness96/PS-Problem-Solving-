# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 13                             | #
# | 14394 9-퍼즐                       | #
# -------------------------------------- #


if __name__ == "__main__":
    current = list(r_input().rstrip())
    aim = list(r_input().rstrip())

    for val in current:
        if val in aim:
            aim.pop(aim.index(val))

    print(len(aim))
