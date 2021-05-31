# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 05                           | #
# | Day 31                             | #
# | 21610 마법사 상어와 비바라기        | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())

    A = [list(map(int, r_input().split())) for _ in range(N)]

    mv = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

    clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

    for _ in range(M):
        d, s = map(int, r_input().split())

        moved_clouds = {}

        for cr, cc in clouds:
            moved_r = (cr + mv[d][0] * s) % N
            moved_c = (cc + mv[d][1] * s) % N

            moved_clouds[(moved_r, moved_c)] = moved_clouds.get((moved_r, moved_c), 0) + 1
            A[moved_r][moved_c] += 1
        
        for loc, val in moved_clouds.items():
            cr, cc = loc
            cnt = 0

            for di in [2, 4, 6, 8]:
                tmp_r = cr + mv[di][0]
                tmp_c = cc + mv[di][1]

                if 0 <= tmp_r < N and 0 <= tmp_c < N:
                    if A[tmp_r][tmp_c]:
                        cnt += val
            
            A[cr][cc] += cnt
        
        new_clouds = []

        for r in range(N):
            for c in range(N):
                if (r, c) not in moved_clouds:
                    if A[r][c] >= 2:
                        new_clouds.append((r, c))
                        A[r][c] -= 2
        
        clouds = new_clouds
    
    total = 0

    for a in A:
        total += sum(a)
    
    print(total)


if __name__ == "__main__":
    run()
