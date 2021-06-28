# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 28                             | #
# | 12845 모두의 마블                    | #
# -------------------------------------- #


if __name__ == "__main__":
    n = int(r_input())
    L = sorted(map(int, r_input().split()))
    result = L[-1] * (n - 1) + sum(L[: -1])

    print(result)
