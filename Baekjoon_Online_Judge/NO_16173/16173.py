# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 15                             | #
# | 16173 점프왕 쩰리 (Small)          | #
# -------------------------------------- #


def jump(row, col):
    if row >= N or col >= N:
        return
    
    if (row, col) == (N - 1, N - 1):
        print('HaruHaru')
        sys.exit()
    
    mv = board[row][col]
    
    if mv == 0:
        return
    
    jump(row, col + mv)
    jump(row + mv, col)


if __name__ == "__main__":
    N = int(r_input())

    board = [list(map(int, r_input().split())) for _ in range(N)]

    jump(0, 0)

    print('Hing')
