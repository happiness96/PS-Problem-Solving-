# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 08                             | #
# | 10709 기상캐스터                    | #
# -------------------------------------- #


if __name__ == "__main__":
    H, W = map(int, r_input().split())

    board = [list(r_input().rstrip()) for _ in range(H)]
    chk = [[-1] * W for _ in range(H)]

    for row in range(H):
        flag = 0
        time = 0

        for col in range(W):
            if board[row][col] == 'c':
                flag = 1
                time = 0
                chk[row][col] = time
            
            elif flag:
                time += 1
                chk[row][col] = time
    
    for c in chk:
        print(*c)
