# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 03                           | #
# | Day 02                             | #
# | 14732 행사장 대여 (Small)          | #
# -------------------------------------- #


def run():
    N = int(r_input())

    board = [[0] * 501 for _ in range(501)]

    for _ in range(N):
        x1, y1, x2, y2 = map(int, r_input().split())
        
        for x in range(x1, x2):
            for y in range(y1, y2):
                board[x][y] = 1
    
    total = 0

    for b in board:
        total += sum(b)
    
    print(total)


if __name__ == "__main__":
    run()
