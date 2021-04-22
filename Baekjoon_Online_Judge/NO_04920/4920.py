# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 22                             | #
# | 4920 테트리스 게임                  | #
# -------------------------------------- #


def run():
    tc = 1

    while True:
        N = int(r_input())

        if not N:
            break

        board = [list(map(int, r_input().split())) for _ in range(N)]
        result = -sys.maxsize
    
        for row in range(N):
            for col in range(N):
                if col <= N - 4:
                    result = max(result, sum(board[row][col: col + 4]))
                
                if row <= N - 4:
                    tot = 0

                    for r in range(row, row + 4):
                        tot += board[r][col]
                    
                    result = max(result, tot)
                
                if row <= N - 2 and col <= N - 2:
                    tot = 0

                    for r in range(row, row + 2):
                        for c in range(col, col + 2):
                            tot += board[r][c]
                    
                    result = max(result, tot)

                if row <= N - 2 and col <= N - 3:
                    tot = board[row][col] + board[row][col + 1] + board[row + 1][col + 1] + board[row + 1][col + 2]

                    result = max(result, tot)

                    tot = sum(board[row][col: col + 3]) + board[row + 1][col + 2]

                    result = max(result, tot)

                    tot = board[row][col] + sum(board[row + 1][col: col + 3])

                    result = max(result, tot)

                    tot = sum(board[row][col: col + 3]) + board[row + 1][col + 1]

                    result = max(result, tot)

                    tot = board[row][col + 1] + sum(board[row + 1][col: col + 3])

                    result = max(result, tot)
                
                if row <= N - 3 and col <= N - 2:
                    tot = board[row][col + 1] + board[row + 1][col] + board[row + 1][col + 1] + board[row + 2][col]

                    result = max(result, tot)

                    tot = board[row][col] + board[row + 1][col] + board[row + 2][col] + board[row][col + 1]

                    result = max(result, tot)

                    tot = board[row + 2][col] + board[row][col + 1] + board[row + 1][col + 1] + board[row + 2][col + 1]

                    result = max(result, tot)

                    tot = board[row][col] + board[row + 1][col] + board[row + 2][col] + board[row + 1][col + 1]

                    result = max(result, tot)

                    tot = board[row][col + 1] + board[row + 1][col + 1] + board[row + 2][col + 1] + board[row + 1][col]

                    result = max(result, tot)

        print(str(tc) + '. ' + str(result))
        
        tc += 1


if __name__ == "__main__":
    run()
