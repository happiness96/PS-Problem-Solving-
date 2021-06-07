# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 04                             | #
# | 21609 상어 중학교                    | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())

    board = [list(map(int, r_input().split())) for _ in range(N)]
    mv = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    total_score = 0

    while True:
        max_basic = []
        max_rainbow = []
        max_cnt = 0
        visit = [[0] * N for _ in range(N)]

        for row in range(N):
            for col in range(N):
                if visit[row][col] or board[row][col] <= 0:
                    continue

                basic = [(row, col)]
                rainbow = []
                
                queue = deque([(row, col)])
                color = board[row][col]
                visit[row][col] = 1
                not_visit = []

                while queue:
                    r, c = queue.popleft()

                    for mv_row, mv_col in mv:
                        tmp_r = r + mv_row
                        tmp_c = c + mv_col

                        if 0 <= tmp_r < N and 0 <= tmp_c < N:
                            if not visit[tmp_r][tmp_c]:
                                visit[tmp_r][tmp_c] = 1

                                if board[tmp_r][tmp_c] == color:
                                    basic.append((tmp_r, tmp_c))
                                    queue.append((tmp_r, tmp_c))
                                
                                elif board[tmp_r][tmp_c] == 0:
                                    rainbow.append((tmp_r, tmp_c))
                                    queue.append((tmp_r, tmp_c))
                                
                                else:
                                    not_visit.append((tmp_r, tmp_c))
                
                total_cnt = len(basic + rainbow)

                if total_cnt > 1:
                    if total_cnt > max_cnt or total_cnt == max_cnt and len(rainbow) >= len(max_rainbow):
                        max_basic = basic
                        max_rainbow = rainbow
                        max_cnt = total_cnt
                
                for r, c in rainbow + not_visit:
                    visit[r][c] = 0
        
        if not max_cnt:
            break

        total_score += max_cnt ** 2

        for r, c in max_basic + max_rainbow:
            board[r][c] = -2
        
        for col in range(N):
            save = []
            minus2 = []
            start_row = N - 1

            for row in range(N - 1, -1, -1):
                if board[row][col] == -2:
                    minus2.append(-2)

                elif board[row][col] == -1:
                    save += minus2

                    for i, val in enumerate(save):
                        board[start_row - i][col] = val
                    
                    start_row = row - 1
                    save = []
                    minus2 = []

                else:
                    save.append(board[row][col])
            
            save += minus2

            for i, val in enumerate(save):
                board[start_row - i][col] = val
    

        new_board = [[0] * N for _ in range(N)]

        for row in range(N):
            for col in range(N):
                new_board[N - row - 1][col] = board[col][row]
        
        board = new_board

        for col in range(N):
            save = []
            minus2 = []
            start_row = N - 1

            for row in range(N - 1, -1, -1):
                if board[row][col] == -2:
                    minus2.append(-2)

                elif board[row][col] == -1:
                    save += minus2

                    for i, val in enumerate(save):
                        board[start_row - i][col] = val
                    
                    start_row = row - 1
                    save = []
                    minus2 = []

                else:
                    save.append(board[row][col])
            
            save += minus2

            for i, val in enumerate(save):
                board[start_row - i][col] = val
    
    print(total_score)


if __name__ == "__main__":
    run()
