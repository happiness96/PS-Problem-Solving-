# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 28                             | #
# | 17388 와글와글 숭고한                | #
# -------------------------------------- #


if __name__ == "__main__":
    S, K, H = map(int, r_input().split())

    if sum((S, K, H)) >= 100:
        print('OK')
    
    else:
        minimum = min(S, K, H)

        if minimum == S:
            print('Soongsil')
        
        elif minimum == K:
            print('Korea')
        
        else:
            print('Hanyang')
