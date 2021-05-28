# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 05                           | #
# | Day 28                             | #
# | 2061 좋은 암호                     | #
# -------------------------------------- #


def run():
    K, L = map(int, r_input().split())

    for number in range(2, L):
        if K % number == 0:
            print('BAD', number)
            sys.exit()
        
    print('GOOD')


if __name__ == "__main__":
    run()
