# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 17                             | #
# | 9322 철벽 보안 알고리즘             | #
# -------------------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        n = int(r_input())

        key1 = list(map(str, r_input().rstrip().split()))
        key2 = list(map(str, r_input().rstrip().split()))

        secret_str = list(map(str, r_input().rstrip().split()))
        result = {}

        for ind in range(n):
            result[key2[ind]] = secret_str[ind]
        
        for val in key1:
            print(result[val], end=' ')
        
        print()


if __name__ == "__main__":
    run()
