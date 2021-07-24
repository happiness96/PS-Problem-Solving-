# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 24                             | #
# | 5063 TGN                           | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    for _ in range(N):
        r, e, c = map(int, r_input().split())

        adv = e - c

        if r > adv:
            print('do not advertise')
        
        elif r < adv:
            print('advertise')
        
        else:
            print('does not matter')
