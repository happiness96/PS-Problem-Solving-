# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 03                           | #
# | Day 10                             | #
# | 17266 어두운 굴다리                | #
# -------------------------------------- #


def run():
    N = int(r_input())
    M = int(r_input())

    x = list(map(int, r_input().split()))

    left, right = 0, N

    while True:
        mid = (left + right) // 2

        if right - left <= 1:
            break

        flag = 1

        for ind in range(1, M):
            if x[ind] - x[ind - 1] > mid * 2:
                flag = 0
                break
        
        if x[0] > mid or N - x[-1] > mid:
            flag = 0

        if flag:
            right = mid
        
        else:
            left = mid

    flag = 1

    for ind in range(1, M):
        if x[ind] - x[ind - 1] > right * 2:
            flag = 0
            break
    
    if x[0] > right or M - x[-1] > right:
        flag = 0
    
    if flag:
        print(right)
    
    else:
        print(left)


if __name__ == "__main__":
    run()
