# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 05                           | #
# | Day 07                             | #
# | 20154 이 구역의 승자는 누구야?!    | #
# -------------------------------------- #


def run():
    S = r_input().rstrip()

    alpha = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]

    save = [alpha[ord(ch) - 65] for ch in S]
    
    print(['You\'re the winner?', 'I\'m a winner!'][sum(save) % 2])


if __name__ == "__main__":
    run()
