# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 28                             | #
# | 21922 학부 연구생 민상               | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())
    board = [list(map(int, r_input().split())) for _ in range(N)]
    visit = [[0] * M for _ in range(N)]

    aircon_locs = []
    flag = 0

    for row in range(N):
        for col in range(M):
            if board[row][col] == 9:
                aircon_locs.append((row, col))
                flag = 1
    
    mv = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    queue = deque([])

    if flag:
        for aircon_loc in aircon_locs:
            for direction in range(4):
                queue.append((aircon_loc[0], aircon_loc[1], direction))
                visit[aircon_loc[0]][aircon_loc[1]] = 1
    
    while queue:
        r, c, d = queue.popleft()

        mv_r, mv_c = mv[d]

        r += mv_r
        c += mv_c

        if 0 <= r < N and 0 <= c < M:
            if board[r][c] == 1:
                if d == 1: d = 3
                elif d == 3: d = 1
            
            elif board[r][c] == 2:
                if d == 0: d = 2
                elif d == 2: d = 0
            
            elif board[r][c] == 3:
                if d == 0: d = 1
                elif d == 1: d = 0
                elif d == 2: d = 3
                elif d == 3: d = 2
            
            elif board[r][c] == 4:
                if d == 0: d = 3
                elif d == 1: d = 2
                elif d == 2: d = 1
                elif d == 3: d = 0
            
            visit[r][c] = 1

            if board[r][c] != 9:
                queue.append((r, c, d))
    
    result = 0
    
    for row in range(N):
        result += sum(visit[row])
    
    print(result)


if __name__ == "__main__":
    run()
