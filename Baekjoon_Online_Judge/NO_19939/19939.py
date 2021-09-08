# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 09                           | #
# | Day 08                             | #
# | 19939 박 터뜨리기                   | #
# -------------------------------------- #


if __name__ == "__main__":
    N, K = map(int, r_input().split())

    total = K * (1 + K) // 2 

    if N < total:
        print(-1)
    
    else:
        N -= total
        print(K - 1 + int(N % K != 0))
