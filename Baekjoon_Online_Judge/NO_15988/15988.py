# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 13                             | #
# | 15988 1, 2, 3 더하기 3             | #
# -------------------------------------- #


def run():
    save = [0, 1, 2, 4]

    for _ in range(1000000):
        save.append((save[-1] + save[-2] + save[-3]) % 1000000009)

    T = int(r_input())

    for _ in range(T):
        n = int(r_input())

        print(save[n])


if __name__ == "__main__":
    run()
