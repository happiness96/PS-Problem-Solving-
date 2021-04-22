# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 21                             | #
# | 20005 보스몬스터 전리품              | #
# -------------------------------------- #


def run():
    M, N, P = map(int, r_input().split())

    board = []
    players_info = {}
    boss_loc = ()

    for row in range(M):
        line = list(r_input().rstrip())
        board.append(line)

        for col in range(N):
            if line[col] == 'B':
                boss_loc = (row, col)
            
            elif line[col] not in '.X':
                players_info[line[col]] = [row, col]

    for _ in range(P):
        player, dps = map(str, r_input().rstrip().split())
        dps = int(dps)
        players_info[player].append(dps)

    boss_hp = int(r_input())
    mv = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    distance_info = {}
    
    for name, info in players_info.items():
        row, col, dps = info

        visit = [[0] * N for _ in range(M)]
        visit[row][col] = 1
        queue = deque([(row, col)])

        distance = 1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for mv_row, mv_col in mv:
                    tmp_row = r + mv_row
                    tmp_col = c + mv_col

                    if 0 <= tmp_row < M and 0 <= tmp_col < N:
                        if not visit[tmp_row][tmp_col]:
                            visit[tmp_row][tmp_col] = 1

                            if board[tmp_row][tmp_col] == 'B':
                                distance_info[distance] = distance_info.get(distance, []) + [dps]
                                queue = []
                                break

                            elif board[tmp_row][tmp_col] != 'X':
                                queue.append((tmp_row, tmp_col))
                
                if not queue:
                    break
            
            distance += 1
    
    result = 0
    tot_dps = 0
    last_time = 0
    
    for time in sorted(distance_info):
        boss_hp -= tot_dps * (time - last_time)

        if boss_hp <= 0:
            break

        tot_dps += sum(distance_info[time])
        last_time = time
        result += len(distance_info[time])
    
    print(result)


if __name__ == "__main__":
    run()
