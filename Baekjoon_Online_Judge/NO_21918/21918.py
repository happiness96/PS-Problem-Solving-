# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 31                             | #
# | 219118 전구                        | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())

    s = list(map(int, r_input().split()))

    for _ in range(M):
        a, b, c = map(int, r_input().split())

        if a == 1:
            s[b - 1] = c
        
        elif a == 2:
            for ind in range(b - 1, c):
                s[ind] = abs(s[ind] - 1)
        
        elif a == 3:
            s[b - 1: c] = [0] * (c - b + 1)
        
        else:
            s[b - 1: c] = [1] * (c - b + 1)
    
    print(*s)


if __name__ == "__main__":
    run()
