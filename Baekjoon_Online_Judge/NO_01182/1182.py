# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 05                           | #
# | Day 15                             | #
# | 1182 부분수열의 합                 | #
# -------------------------------------- #


def select(ind, total):
    global result

    total += numbers[ind]
    
    if total == S:
        result += 1
    
    for i in range(ind + 1, N):
        select(i, total)


if __name__ == "__main__":
    N, S = map(int, r_input().split())

    numbers = sorted(map(int, r_input().split()))

    result = 0

    for ind in range(N):
        select(ind, 0)
    
    print(result)
