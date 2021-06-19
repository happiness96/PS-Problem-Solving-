# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 19                             | #
# | 1012 유기농 배추                   | #
# -------------------------------------- #


if __name__ == "__main__":
    T = int(r_input())
    mv = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    for _ in range(T):
        M, N, K = map(int, r_input().split())
        board = [[0] * N for _ in range(M)]

        for _ in range(K):
            X, Y = map(int, r_input().split())
            board[X][Y] = 1
    
        visit = [[0] * N for _ in range(M)]
        visit[0][0] = 1
        result = 0

        for x in range(M):
            for y in range(N):
                if board[x][y] and not visit[x][y]:
                    queue = deque([(x, y)])
                    visit[x][y] = 1
                    result += 1

                    while queue:
                        xx, yy = queue.popleft()

                        for mv_x, mv_y in mv:
                            tmp_x = xx + mv_x
                            tmp_y = yy + mv_y

                            if 0 <= tmp_x < M and 0 <= tmp_y < N:
                                if board[tmp_x][tmp_y] and not visit[tmp_x][tmp_y]:
                                    visit[tmp_x][tmp_y] = 1
                                    queue.append((tmp_x, tmp_y))
        
        print(result)
