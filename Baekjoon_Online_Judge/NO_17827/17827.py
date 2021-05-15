# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 05                           | #
# | Day 15                             | #
# | 17827 달팽이 리스트                 | #
# -------------------------------------- #


def run():
    N, M, V = map(int, r_input().split())

    C = list(map(int, r_input().split()))

    cycle_length = N - V + 1

    for _ in range(M):
        K = int(r_input())

        if K < V:
            print(C[K])
        
        else:
            K -= (V - 1)
            K %= cycle_length

            print(C[V - 1 + K])


if __name__ == "__main__":
    run()
