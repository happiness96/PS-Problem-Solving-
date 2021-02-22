# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 22                             | #
# | 9455 박스                          | #
# -------------------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        m, n = map(int, r_input().split())

        board = [list(map(int, r_input().split())) for _ in range(m)]

        res = 0

        for col in range(n):
            zero_cnt = 0

            for row in range(m - 1, -1, -1):
                if board[row][col]:
                    res += zero_cnt
                
                else:
                    zero_cnt += 1
        
        print(res)


if __name__ == "__main__":
    run()
