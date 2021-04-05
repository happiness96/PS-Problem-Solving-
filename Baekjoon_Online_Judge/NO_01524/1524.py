# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 05                             | #
# | 1524 세준세비                       | #
# -------------------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        r_input()

        N, M = map(int, r_input().split())

        jun = sorted(map(int, r_input().split()))[::-1]
        bi = sorted(map(int, r_input().split()))[::-1]

        while jun and bi:
            if jun[-1] > bi[-1]:
                bi.pop()
            
            elif jun[-1] < bi[-1]:
                jun.pop()
            
            else:
                bi.pop()
            
        print('S' if jun else 'B')


if __name__ == "__main__":
    run()
