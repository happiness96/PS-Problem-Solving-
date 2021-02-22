# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 22                             | #
# | 1592 영식이와 친구들                | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M, L = map(int, r_input().split())

    L %= N

    rec = [0] * (N + 1)
    rec[1] += 1

    loc = 1
    cnt = 0

    while True:
        if rec[loc] % 2:
            loc += L

            if loc > N:
                loc -= N
        
        else:
            loc -= L
            
            if loc < 1:
                loc += N
            
        rec[loc] += 1
        cnt += 1
        
        if rec[loc] == M:
            print(cnt)
            break
