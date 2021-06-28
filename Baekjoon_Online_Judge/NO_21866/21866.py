# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 26                             | #
# | 21866 추첨을 통해 커피를 받자        | #
# -------------------------------------- #


if __name__ == "__main__":
    scores = list(map(int, r_input().split()))
    max_score = [100, 100, 200, 200, 300, 300, 400, 400, 500]

    for ind, score in enumerate(scores):
        if score > max_score[ind]:
            print('hacker')
            sys.exit()
    
    if sum(scores) >= 100:
        print('draw')
    
    else:
        print('none')
