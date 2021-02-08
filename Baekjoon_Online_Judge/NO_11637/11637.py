# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 08                             | #
# | 11637 인기 투표                    | #
# -------------------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for _ in range(T):
        n = int(r_input())
        vote = [int(r_input()) for _ in range(n)]

        maximum = max(vote)

        if vote.count(maximum) > 1:
            print('no winner')
        
        elif maximum > sum(vote) // 2:
            print('majority winner', vote.index(maximum) + 1)
        
        else:
            print('minority winner', vote.index(maximum) + 1)
