# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 08                             | #
# | 4108 지뢰찾기                      | #
# -------------------------------------- #


def run():
    mv = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    while True:
        R, C = map(int, r_input().split())

        if R == C == 0:
            break

        board = [r_input().rstrip() for _ in range(R)]
        chk = [['*'] * C for _ in range(R)]

        for row in range(R):
            for col in range(C):
                if board[row][col] == '*':
                    continue

                cnt = 0

                for mv_row, mv_col in mv:
                    tmp_row = row + mv_row
                    tmp_col = col + mv_col

                    if 0 <= tmp_row < R and 0 <= tmp_col < C:
                        if board[tmp_row][tmp_col] == '*':
                            cnt += 1
                
                chk[row][col] = str(cnt)
    
        for c in chk:
            print(''.join(c))


if __name__ == "__main__":
    run()
