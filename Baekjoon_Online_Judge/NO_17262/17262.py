# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 05                           | #
# | Day 31                             | #
# | 17262 팬덤이 넘쳐흘러               | #
# -------------------------------------- #


def run():
    N = int(r_input())

    last_S = 0
    first_E = sys.maxsize

    for _ in range(N):
        s, e = map(int, r_input().split())
        
        last_S = max(last_S, s)
        first_E = min(first_E, e)
    
    print(max(0, last_S - first_E))


if __name__ == "__main__":
    run()
