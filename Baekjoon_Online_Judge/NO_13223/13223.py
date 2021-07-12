# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 12                             | #
# | 13223 소금 폭탄                     | #
# -------------------------------------- #


def run():
    cur_h, cur_m, cur_s = map(int, r_input().split(':'))
    bomb_h, bomb_m, bomb_s = map(int, r_input().split(':'))

    bomb_s -= cur_s
    
    if bomb_s < 0:
        bomb_s += 60
        bomb_m -= 1
    
    bomb_m -= cur_m

    if bomb_m < 0:
        bomb_m += 60
        bomb_h -= 1

    bomb_h -= cur_h

    if bomb_h < 0:
        bomb_h += 24

    if bomb_h == bomb_m == bomb_s == 0:
        bomb_h = 24

    print('%02d:%02d:%02d' % (bomb_h, bomb_m, bomb_s))


if __name__ == "__main__":
    run()
