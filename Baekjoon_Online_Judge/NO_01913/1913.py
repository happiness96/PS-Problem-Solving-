# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 03                           | #
# | Day 02                             | #
# | 1913 달팽이                        | #
# -------------------------------------- #


def run():
    N = int(r_input())
    M = int(r_input())

    board = [[0] * N for _ in range(N)]

    row, col = N // 2, N // 2
    number = 1
    step = 1

    board[row][col] = number

    for _ in range(N // 2):
        for _ in range(step):
            row -= 1
            number += 1
            board[row][col] = number
        
        for _ in range(step):
            col += 1
            number += 1
            board[row][col] = number
        
        step += 1

        for _ in range(step):
            row += 1
            number += 1
            board[row][col] = number
        
        for _ in range(step):
            col -= 1
            number +=1
            board[row][col] = number
        
        step += 1
    
    for _ in range(step - 1):
        row -= 1
        number += 1
        board[row][col] = number
    
    for b in board:
        print(*b)
    
    for r in range(N):
        for c in range(N):
            if board[r][c] == M:
                print(r + 1, c + 1)
                sys.exit()


if __name__ == "__main__":
    run()
