# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 05                           | #
# | Day 25                             | #
# | 20500 Ezreal 여눈부터 가네 ㅈㅈ     | #
# -------------------------------------- #


if __name__ == "__main__":
    result = [0]

    N = int(r_input())

    for i in range(1515):
        if i % 2:
            result.append((sum(result) + 1) % 1000000007)
        
        else:
            result.append(sum(result) % 1000000007)
        
    print(result[N])
