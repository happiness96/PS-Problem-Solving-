# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 28                             | #
# | 20540 연길이의 이상형                | #
# -------------------------------------- #


if __name__ == "__main__":
    save = {'E': 'I', 'I': 'E', 'S': 'N', 'N': 'S', 
    'T': 'F', 'F': 'T', 'J': 'P', 'P': 'J'}

    mbti = r_input().rstrip()

    for ch in mbti:
        print(save[ch], end='')
