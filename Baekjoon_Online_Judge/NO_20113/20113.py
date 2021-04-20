# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 20                             | #
# | 20113 긴급 회의                      | #
# -------------------------------------- #


def run():
    N = int(r_input())

    X = list(map(int, r_input().split()))
    cnt = [0] * (N + 1)

    for val in X:
        if val:
            cnt[val] += 1
    
    maximum = max(cnt)

    if cnt.count(maximum) > 1:
        print('skipped')
    
    else:
        print(cnt.index(maximum))


if __name__ == "__main__":
    run()
