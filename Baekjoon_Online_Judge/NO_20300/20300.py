# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 20                             | #
# | 20300 서강근육맨                    | #
# -------------------------------------- #


def run():
    N = int(r_input())

    t = deque(sorted(map(int, r_input().split())))

    maximum = 0

    if N % 2:
        maximum = t.pop()

    while t:
        maximum = max(maximum, t.popleft() + t.pop())
    
    print(maximum)


if __name__ == "__main__":
    run()
