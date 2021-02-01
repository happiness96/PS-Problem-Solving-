# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 01                             | #
# | 19947 투자의 귀재 배주형            | #
# -------------------------------------- #


def find_result(money, rem_year):
    if rem_year == 0:
        return money
    
    save = []

    if rem_year >= 1:
        save.append(find_result(int(money * 1.05), rem_year - 1))
    
    if rem_year >= 3:
        save.append(find_result(int(money * 1.2), rem_year - 3))
    
    if rem_year >= 5:
        save.append(find_result(int(money * 1.35), rem_year - 5))
    
    return(max(save))


if __name__ == "__main__":
    H, Y = map(int, r_input().split())

    result = 0

    result = find_result(H, Y)

    print(result)
