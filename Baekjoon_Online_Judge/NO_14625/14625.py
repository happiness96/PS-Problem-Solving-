# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 05                             | #
# | 14625 냉동식품                      | #
# -------------------------------------- #


if __name__ == "__main__":
    start_h, start_m = map(int, r_input().split())
    end_h, end_m = map(int, r_input().split())
    N = int(r_input())
    result = 0

    while True:
        if str(N) in '%02d%02d' % (start_h, start_m):
            result += 1
        
        if start_h == end_h and start_m == end_m:
            break
        
        start_m += 1

        if start_m == 60:
            start_m = 0
            start_h += 1
    
    print(result)
