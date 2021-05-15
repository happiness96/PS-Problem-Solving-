# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 05                           | #
# | Day 15                             | #
# | 16162 가희와 3단 고음               | #
# -------------------------------------- #


if __name__ == "__main__":
    N, A, D = map(int, r_input().split())

    sounds = list(map(int, r_input().split()))

    X = 0

    for sound in sounds:
        if sound == A + D * X:
            X += 1
    
    print(X)
