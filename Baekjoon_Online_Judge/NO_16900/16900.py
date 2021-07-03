# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 03                             | #
# | 16900 이름 정하기                   | #
# -------------------------------------- #


def run():
    S, K = map(str, r_input().split())
    K = int(K)
    
    len_S = len(S)

    pi = [0] * len_S

    i = 0
    j = 1

    while j < len_S:
        if S[i] == S[j]:
            i += 1
            pi[j] = i
            j += 1
        
        else:
            if i == 0:
                j += 1
            
            else:
                i = pi[i - 1]

    print((len_S - pi[-1]) * K + pi[-1])


if __name__ == "__main__":
    run()
