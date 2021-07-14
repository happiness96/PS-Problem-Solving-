# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 14                             | #
# | 20002 사과나무                      | #
# -------------------------------------- #


def run():
    N = int(r_input())
    board = [[0] * (N + 1)]

    for _ in range(N):
        board.append([0] + list(map(int, r_input().split())))
    
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            board[row][col] += board[row - 1][col] + board[row][col - 1] - board[row - 1][col - 1]
    
    result = -1000

    for row in range(1, N + 1):
        for col in range(1, N + 1):
            K_max = min(N - row, N - col) + 1
            
            for k in range(K_max):
                result = max(result, board[row + k][col + k] - board[row - 1][col + k] - board[row + k][col - 1] + board[row - 1][col - 1])
    
    print(result)


if __name__ == "__main__":
    run()
