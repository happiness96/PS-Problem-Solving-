# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 26                             | #
# | 10844 쉬운 계단 수                  | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    
    result = [1] * 10
    result[0] = 0

    for _ in range(N - 1):
        new_result = [0] * 10

        for ind in range(1, 9):
            new_result[ind - 1] += result[ind]
            new_result[ind + 1] += result[ind]
        
        new_result[1] += result[0]
        new_result[-2] += result[-1]

        result = new_result
    
    print(sum(result) % 1000000000)
