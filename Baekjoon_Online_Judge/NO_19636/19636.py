# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 20                             | #
# | 19636 요요 시뮬레이션               | #
# -------------------------------------- #


if __name__ == "__main__":
    W, I1, T = map(int, r_input().split())
    D, I2, A = map(int, r_input().split())

    plus = I2 - I1 - A
    origin_I1 = I1

    if W + plus * D <= 0:
        print('Danger Diet')
    
    else:
        print(W + plus * D, I1)

    danger = 0

    for _ in range(D):
        plus = I2 - I1 - A
        W += plus

        if abs(plus) > T:
            I1 += plus // 2

        if W <= 0 or I1 <= 0:
            danger = 1
            break
    
    if danger:
        print('Danger Diet')
    
    else:
        print(W, I1, end=' ')
        
        if I1 == origin_I1:
            print('NO')
        
        else:
            print('YOYO')
