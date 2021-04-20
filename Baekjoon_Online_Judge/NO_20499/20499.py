# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 20                             | #
# | 20499 Darius님 한타 안 함?          | #
# -------------------------------------- #


if __name__ == "__main__":
    K, D, A = map(int, r_input().split('/'))

    if K + A < D or not D:
        print('hasu')
    
    else:
        print('gosu')
