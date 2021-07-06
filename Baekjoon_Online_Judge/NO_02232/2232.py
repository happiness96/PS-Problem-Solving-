# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 06                             | #
# | 2232 지뢰                          | #
# -------------------------------------- #


def run():
    N = int(r_input())

    P_list = [0] + [int(r_input()) for _ in range(N)] + [0]

    for ind in range(1, N + 1):
        if P_list[ind - 1] <= P_list[ind] and P_list[ind + 1] <= P_list[ind]:
            print(ind)


if __name__ == "__main__":
    run()
