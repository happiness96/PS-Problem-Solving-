# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 22                             | #
# | 5566 주사위 게임                   | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())
    board = [int(r_input()) for _ in range(N)]
    loc = 0

    for cnt in range(1, M + 1):
        number = int(r_input())

        loc += number

        if loc < N:
            loc += board[loc]
        
        if loc >= N - 1:
            print(cnt)
            break
