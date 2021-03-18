# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 03                           | #
# | Day 15                             | #
# | 15658 연산자 끼워넣기 (2)           | #
# -------------------------------------- #


def calculate(ind, res):
    global maximum, minimum

    if ind == N - 1:
        maximum = max(res, maximum)
        minimum = min(res, minimum)
        return
    
    for sign_ind, sign in enumerate('+-*/'):
        if count[sign_ind] < signs[sign_ind]:
            count[sign_ind] += 1
            
            if sign_ind == 0:
                calculate(ind + 1, res + A[ind + 1])
            
            elif sign_ind == 1:
                calculate(ind + 1, res - A[ind + 1])
            
            elif sign_ind == 2:
                calculate(ind + 1, res * A[ind + 1])
            
            else:
                if res < 0:
                    calculate(ind + 1, -(-res // A[ind + 1]))
                
                else:
                    calculate(ind + 1, res // A[ind + 1])
            
            count[sign_ind] -= 1


if __name__ == "__main__":
    N = int(r_input())
    A = list(map(int, r_input().split()))
    signs = list(map(int, r_input().split()))

    maximum = -1000000000
    minimum = 1000000000

    count = [0, 0, 0, 0]

    calculate(0, A[0])

    print(maximum)
    print(minimum)
