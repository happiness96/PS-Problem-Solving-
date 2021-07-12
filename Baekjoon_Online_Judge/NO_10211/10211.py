# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 12                             | #
# | 10211 Maximum Subarray             | #
# -------------------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        N = int(r_input())

        result = -1000

        save = 0

        for number in map(int, r_input().split()):
            save += number

            result = max(result, save)

            if save < 0:
                save = 0
        
        print(result)


if __name__ == "__main__":
    run()
