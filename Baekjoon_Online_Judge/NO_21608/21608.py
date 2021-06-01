# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 05                           | #
# | Day 31                             | #
# | 21608 상어 초등학교                | #
# -------------------------------------- #


def run():
    N = int(r_input())

    seat = [[0] * N for _ in range(N)]
    st_info = {}

    for _ in range(N ** 2):
        st_no, *st_like = list(map(int, r_input().split()))
        st_info[st_no] = st_like

        max_like_cnt = -1
        max_blank_cnt = -1
        my_seat = (0, 0)

        for row in range(N):
            for col in range(N):
                if seat[row][col]:
                    continue

                like_cnt = 0
                blank_cnt = 0

                for mv_row, mv_col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    tmp_row = row + mv_row
                    tmp_col = col + mv_col

                    if 0 <= tmp_row < N and 0 <= tmp_col < N:
                        if not seat[tmp_row][tmp_col]:
                            blank_cnt += 1

                        if seat[tmp_row][tmp_col] in st_like:
                            like_cnt += 1
                
                if max_like_cnt < like_cnt:
                    max_like_cnt = like_cnt
                    max_blank_cnt = blank_cnt
                    my_seat = (row, col)
                
                elif max_like_cnt == like_cnt:
                    if max_blank_cnt < blank_cnt:
                        max_blank_cnt = blank_cnt
                        my_seat = (row, col)
                    
        seat[my_seat[0]][my_seat[1]] = st_no

    result = 0
    
    for row in range(N):
        for col in range(N):
            st_no = seat[row][col]
            
            like_cnt = 0

            for mv_row, mv_col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                tmp_row = row + mv_row
                tmp_col = col + mv_col

                if 0 <= tmp_row < N and 0 <= tmp_col < N:
                    if seat[tmp_row][tmp_col] in st_info[st_no]:
                        like_cnt += 1

            if like_cnt:
                result += 1 * 10 ** (like_cnt - 1)
    
    print(result)


if __name__ == "__main__":
    run()
