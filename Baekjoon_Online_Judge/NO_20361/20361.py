# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 28                             | #
# | 20361 일우는 야바위꾼                | #
# -------------------------------------- #


def run():
    N, X, K = map(int, r_input().split())

    for _ in range(K):
        A, B = map(int, r_input().split())

        if X == A:
            X = B
        
        elif X == B:
            X = A
    
    print(X)


if __name__ == "__main__":
    run()
