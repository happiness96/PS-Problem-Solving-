# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 28                             | #
# | 20155 우리 집 밑에 편의점이 있는데   | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())

    X_count = {}

    for X in map(int, r_input().split()):
        X_count[X] = X_count.get(X, 0) + 1
    
    print(max(X_count.values()))
