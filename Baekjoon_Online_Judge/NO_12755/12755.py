# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 06                             | #
# | 12755 수면 장애                     | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    zero_cnt = 0
    while True:
        cnt = (zero_cnt + 1) * 9 * 10 ** zero_cnt
        
        if N > cnt:
            N -= cnt
        
        else:
            number = 10 ** zero_cnt + N // (zero_cnt + 1)
            rem = N % (zero_cnt + 1)

            if not rem:
                print(str(number - 1)[-1])
            
            else:
                print(str(number)[rem - 1])
            break
        
        zero_cnt += 1
