# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 03                           | #
# | Day 02                             | #
# | 11478 서로 다른 부분 문자열         | #
# -------------------------------------- #


def run():
    S = r_input().rstrip()

    save = []
    idx = 0

    for ch in S:
        save.append('')
        finish = len(save)

        for ind in range(idx, finish):
            save.append(save[ind] + ch)
            idx += 1
    
    print(len(set(save)) - 1)


if __name__ == "__main__":
    run()