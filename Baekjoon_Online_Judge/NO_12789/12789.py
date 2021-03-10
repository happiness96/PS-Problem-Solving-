# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 03                           | #
# | Day 10                             | #
# | 12789 도키도키 간식드리미           | #
# -------------------------------------- #


def run():
    N = int(r_input())

    numbers = list(map(int, r_input().split()))
    temp = []

    turn = 1

    for number in numbers:
        if number == turn:
            turn += 1

            while temp and temp[-1] == turn:
                temp.pop()
                turn += 1
        
        else:
            temp.append(number)
    
    for number in temp[::-1]:
        if number == turn:
            turn += 1
    
    if turn == N + 1:
        print('Nice')
    
    else:
        print('Sad')


if __name__ == "__main__":
    run()
