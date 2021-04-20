# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 20                             | #
# | 20207 달력                          | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    S_list = []
    E_list = []

    for _ in range(N):
        S, E = map(int, r_input().split())

        S_list.append(S)
        E_list.append(E)
    
    S_list.sort(reverse=True)
    E_list.sort(reverse=True)

    result = 0
    start = S_list[-1]
    last = E_list[-1]
    height = 0
    max_height = 0
    flag = 0

    for day in range(1, 366):
        if not height and S_list and S_list[-1] != day:
            flag = 1

        while S_list and S_list[-1] == day:
            if not height and flag:
                result += max_height * (last - start + 1)
                start = day
                last = day
                max_height = 0
                flag = 0

            S_list.pop()
            height += 1
            max_height = max(max_height, height)
        
        while E_list and E_list[-1] == day:
            last = E_list.pop()
            height -= 1
    
    result += max_height * (last - start + 1)
    print(result)
