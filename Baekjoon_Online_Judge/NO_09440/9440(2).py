# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 01                             | #
# | 9440 숫자 더하기                    | #
# -------------------------------------- #


if __name__ == "__main__":
    while True:
        N, *numbers = map(str, r_input().split())

        if N == '0':
            break

        numbers.sort()
        
        number1 = ''
        number2 = ''

        zero = numbers.count('0')
        numbers = numbers[zero:]
        
        number1 += numbers[0]
        number2 += numbers[1]

        for i in range(zero):
            if i % 2 == 0:
                number1 += '0'
            
            else:
                number2 += '0'
            
        for i in range(2, int(N) - zero):
            if i % 2 == 0 + zero % 2:
                number1 += numbers[i]
            
            else:
                number2 += numbers[i]
        
        print(int(number1) + int(number2))
