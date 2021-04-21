# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 20                             | #
# | 20208 진우의 민트초코우유           | #
# -------------------------------------- #


def find_milk(cur_loc, rem):
    global result

    if abs(cur_loc[0] - JW_LOC[0]) + abs(cur_loc[1] - JW_LOC[1]) <= rem:
        result = max(result, sum(visit))
    
    for ind in range(milk_cnt):
        if not visit[ind]:
            distance = abs(cur_loc[0] - milk_locs[ind][0]) + abs(cur_loc[1] - milk_locs[ind][1])

            if distance <= rem:
                visit[ind] = 1
                find_milk(milk_locs[ind], rem - distance + H)
                visit[ind] = 0


if __name__ == "__main__":
    N, M, H = map(int, r_input().split())

    board = []
    JW_LOC = ()
    milk_locs = []

    for row in range(N):
        line = list(map(int, r_input().split()))
        board.append(line)

        for col in range(N):
            if line[col] == 1:
                JW_LOC = (row, col)
            
            if line[col] == 2:
                milk_locs.append((row, col))
    
    milk_cnt = len(milk_locs)
    visit = [0] * milk_cnt
    result = 0

    find_milk(JW_LOC, M)

    print(result)
