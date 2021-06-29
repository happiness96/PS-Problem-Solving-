# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 29                             | #
# | 16570 앞뒤가 맞는 수열              | #
# -------------------------------------- #


def run():
    N = int(r_input())

    A = list(map(int, r_input().split()))[::-1]
    length_A = len(A)

    i = 0
    j = 1
    pi = [0] * length_A

    while j < N:
        if A[i] == A[j]:
            i += 1
            pi[j] = i
            j += 1
        
        else:
            if i == 0:
                j += 1
            
            else:
                i = pi[i - 1]
    
    maximum = max(pi)

    if maximum:
        print(maximum, pi.count(maximum))
    
    else:
        print(-1)


if __name__ == "__main__":
    run()
