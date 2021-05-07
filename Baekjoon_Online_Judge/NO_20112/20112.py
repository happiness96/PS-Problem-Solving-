# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 05                           | #
# | Day 07                             | #
# | 20112 사토르 마방진                 | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    board = [r_input().rstrip() for _ in range(N)]
    flag = 1

    for row in range(N):
        for col in range(row + 1, N):
            if board[row][col] != board[col][row]:
                print('NO')
                sys.exit()
    
    print('YES')
