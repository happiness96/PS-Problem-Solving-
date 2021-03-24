# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 03                           | #
# | Day 24                             | #
# | 10974 모든 순열                     | #
# -------------------------------------- #


def select_number(save):
    if len(save) == N:
        print(*save)
        return
    
    for ind in range(1, N + 1):
        if not visit[ind]:
            visit[ind] = 1
            select_number(save + [ind])
            visit[ind] = 0


if __name__ == "__main__":
    N = int(r_input())

    visit = [0] * (N + 1)
    
    select_number([])