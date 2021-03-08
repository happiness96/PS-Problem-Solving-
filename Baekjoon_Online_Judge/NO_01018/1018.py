# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 03                           | #
# | Day 08                             | #
# | 1018 체스판 다시 칠하기             | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())

    board = [r_input().rstrip() for _ in range(N)]
    cmp_board1 = [['B'] * 8 for _ in range(8)]
    cmp_board2 = [['B'] * 8 for _ in range(8)]

    for row in range(8):
        for col in range(8):
            if row % 2 and col % 2 or row % 2 == 0 and col % 2 == 0:
                cmp_board1[row][col] = 'W'
            
            else:
                cmp_board2[row][col] = 'W'

    result = sys.maxsize

    for start_row in range(N - 7):
        for start_col in range(M - 7):
            cnt1 = 0

            for row in range(8):
                for col in range(8):
                    if board[start_row + row][start_col + col] != cmp_board1[row][col]:
                        cnt1 += 1
            
            cnt2 = 0

            for row in range(8):
                for col in range(8):
                    if board[start_row + row][start_col + col] != cmp_board2[row][col]:
                        cnt2 += 1
            
            result = min(result, cnt1, cnt2)

    print(result)
