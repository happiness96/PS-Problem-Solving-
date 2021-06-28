# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 28                             | #
# | 5547 일루미네이션                    | #
# -------------------------------------- #


def run():
    W, H = map(int, r_input().split())

    board = [[0] * (W + 2)]

    for _ in range(H):
        board.append([0] + list(map(int, r_input().split())) + [0])
    
    board.append([0] * (W + 2))

    total = 0

    mv = [[(0, 1), (0, -1), (-1, 0), (-1, -1), (1, 0), (1, -1)], [(0, 1), (0, -1), (-1, 0), (-1, 1), (1, 0), (1, 1)]]

    queue = deque([(0, 0)])
    board[0][0] = 2

    while queue:
        r, c = queue.popleft()

        for mv_r, mv_c in mv[r % 2]:
            tmp_r = r + mv_r
            tmp_c = c + mv_c
            
            if 0 <= tmp_r < (H + 2) and 0 <= tmp_c < (W + 2):
                if board[tmp_r][tmp_c] == 1:
                    total += 1
                
                elif board[tmp_r][tmp_c] == 0:
                    queue.append((tmp_r, tmp_c))
                    board[tmp_r][tmp_c] = 2
    
    print(total)


if __name__ == "__main__":
    run()
