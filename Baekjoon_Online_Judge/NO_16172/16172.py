# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 28                             | #
# | 16172 나는 친구가 적다 (Large)      | #
# -------------------------------------- #


def run():
    S = ""

    for ch in r_input().rstrip():
        if ch not in '0123456789':
            S += ch
    
    K = r_input().rstrip()

    length_S = len(S)
    length_K = len(K)

    pi = [0] * length_K

    i = 0
    j = 1

    while j < length_K:
        if K[i] == K[j]:
            i += 1
            pi[j] = i
            j += 1
        
        else:
            if i == 0:
                j += 1
            
            else:
                i = pi[i - 1]
    
    i = 0
    j = 0

    while i < length_S:
        if S[i] == K[j]:
            i += 1
            j += 1
        
        else:
            if j == 0:
                i += 1
            
            else:
                j = pi[j - 1]
        
        if j == length_K:
            print(1)
            sys.exit()
    
    print(0)


if __name__ == "__main__":
    run()
