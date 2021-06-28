# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 26                             | #
# | 21966 (중략)                       | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    S = r_input().rstrip()

    length = len(S)

    if length <= 25:
        print(S)
    
    else:
        middle = S[11: -11]
        chk = middle[: -1].count('.')

        if chk:
            print(S[: 9] + '......' + S[-10:])
        
        else:
            print(S[: 11] + '...' + S[-11:])
