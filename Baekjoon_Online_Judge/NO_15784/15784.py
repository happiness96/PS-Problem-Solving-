# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 12                             | #
# | 15784 질투진서                      | #
# -------------------------------------- #


def run():
    N, a, b = map(int, r_input().split())

    a -= 1
    b -= 1

    max_col = 0
    tmp = 0

    for ind in range(N):
        line = list(map(int, r_input().split()))
        max_col = max(max_col, line[b])

        if ind == a:
            tmp = line[b]

            if max(line) != tmp or max_col != tmp:
                print('ANGRY')
                sys.exit()
    
    if max_col != tmp:
        print('ANGRY')
    
    else:
        print('HAPPY')


if __name__ == "__main__":
    run()
