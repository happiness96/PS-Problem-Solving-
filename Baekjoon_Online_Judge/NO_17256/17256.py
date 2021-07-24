# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 24                             | #
# | 17256 달달함이 넘쳐흘러             | #
# -------------------------------------- #


if __name__ == "__main__":
    ax, ay, az = map(int, r_input().split())
    cx, cy, cz = map(int, r_input().split())

    print(cx - az, cy // ay, cz - ax)
