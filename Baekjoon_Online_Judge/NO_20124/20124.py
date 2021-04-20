# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 20                             | #
# | 20124 모르고리즘 회장님 추천 받습니다 | #
# -------------------------------------- #


def run():
    N = int(r_input())

    result = ''
    score = 0

    for _ in range(N):
        A, B = map(str, r_input().rstrip().split())
        B = int(B)

        if B > score:
            score = B
            result = A
        
        elif B == score:
            result = min(result, A)
    
    print(result)


if __name__ == "__main__":
    run()
