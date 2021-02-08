# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 08                             | #
# | 2799 블라인드                      | #
# -------------------------------------- #


if __name__ == "__main__":
    M, N = map(int, r_input().split())
    board = [r_input().rstrip() for _ in range(5 * M + 1)]
    result = [0] * 5

    window = ['................', '****............', '********........', '************....', '****************']

    for start_row in range(1, 5 * M + 1, 5):
        for start_col in range(1, 5 * N + 1, 5):
            save = ''

            for k in range(4):
                save += board[start_row + k][start_col: start_col + 4]
            
            for i, val in enumerate(window):
                if val == save:
                    result[i] += 1
    
    print(*result)
