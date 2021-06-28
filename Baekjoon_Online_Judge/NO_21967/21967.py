# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 26                             | #
# | 21967 세워라 반석 위에              | #
# -------------------------------------- #


def run():
    N = int(r_input())

    A = list(map(int, r_input().split()))

    i = 0
    j = 0

    dp = [0] * 11
    result = 0

    while j < N:
        dp[A[j]] += 1

        minimum = 10
        maximum = 0

        for ind, val in enumerate(dp):
            if val:
                maximum = max(maximum, ind)
                minimum = min(minimum, ind)
        
        j += 1
        
        while maximum - minimum > 2:
            dp[A[i]] -= 1

            minimum = 10
            maximum = 0

            for ind, val in enumerate(dp):
                if val:
                    maximum = max(maximum, ind)
                    minimum = min(minimum, ind)
            
            i += 1
        
        result = max(result, j - i)
    
    print(result)


if __name__ == "__main__":
    run()
