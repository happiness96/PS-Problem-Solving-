# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 12                             | #
# | 19564 반복                          | #
# -------------------------------------- #


def run():
    S = r_input().rstrip()

    K = 1

    for ind in range(1, len(S)):
        if S[ind] <= S[ind - 1]:
            K += 1
    
    print(K)


if __name__ == "__main__":
    run()
