# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 03                           | #
# | Day 02                             | #
# | 14726 신용카드 판별                 | #
# -------------------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for _ in range(T):
        card_number = r_input().rstrip()
        tot = 0

        for i in range(15, -1, -1):
            if i % 2 == 0:
                number = int(card_number[i]) * 2

                if number >= 10:
                    number = number % 10 + number // 10
                
                tot += number
            
            else:
                tot += int(card_number[i])
        
        if tot % 10:
            print('F')
        
        else:
            print('T')
