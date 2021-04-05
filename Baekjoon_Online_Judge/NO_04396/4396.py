# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 05                             | #
# | 4396 지뢰 찾기                      | #
# -------------------------------------- #


def run():
    N = int(r_input())

    board = [r_input().rstrip() for _ in range(N)]
    playing = [list(r_input().rstrip()) for _ in range(N)]

    mv =[(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]

    opened = 0

    for row in range(N):
        for col in range(N):
            if playing[row][col] == 'x' and board[row][col] == '*':
                opened = 1
                break
        
        if opened:
            break
    
    for row in range(N):
        for col, val in enumerate(playing[row]):
            if opened and board[row][col] == '*':
                playing[row][col] = '*'
                continue
            
            if val == 'x':                
                count = 0

                for dr, dc in mv:
                    tmp_row = row + dr
                    tmp_col = col + dc

                    if 0 <= tmp_row < N and 0 <= tmp_col < N:
                        if board[tmp_row][tmp_col] == '*':
                            count += 1
                
                playing[row][col] = str(count)
    
    for res in playing:
        print(''.join(res))


if __name__ == "__main__":
    run()
