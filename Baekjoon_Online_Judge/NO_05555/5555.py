# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 05                             | #
# | 5555 반지                          | #
# -------------------------------------- #


if __name__ == "__main__":
    string = r_input().rstrip()
    res = 0
    N = int(r_input())

    for _ in range(N):
        ring = r_input().rstrip()

        if string in ring * 2:
            res += 1
    
    print(res)