# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 28                             | #
# | 1787 문자열의 주기 예측              | #
# -------------------------------------- #


def run():
    n = int(r_input())

    S = r_input().rstrip()

    pi = [0] * n

    i = 0
    j = 1
    result = 0

    while j < n:
        if S[i] == S[j]:
            if pi[i] == 0:
                pi[j] = i + 1
            
            else:
                pi[j] = pi[i]
            
            i += 1
            j += 1

            result += j - pi[j - 1]
        
        else:
            if i == 0:
                j += 1
            
            else:
                i = pi[i - 1]
                
    print(result)


if __name__ == "__main__":
    run()
