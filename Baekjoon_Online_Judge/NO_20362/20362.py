# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 06                             | #
# | 20362 유니대전 퀴즈쇼               | #
# -------------------------------------- #


if __name__ == "__main__":
    N, S = r_input().rstrip().split()
    N = int(N)

    log = {}

    for _ in range(N):
        name, answer = r_input().rstrip().split()

        if name == S:
            print(log.get(answer, 0))
            break

        log[answer] = log.get(answer, 0) + 1
