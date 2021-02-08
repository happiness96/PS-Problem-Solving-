# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 08                             | #
# | 14654 스테판 쿼리                   | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    A = list(map(int, r_input().split()))
    B = list(map(int, r_input().split()))

    who_win = 0
    win = 0
    result = 0

    win_case = [(1, 2), (2, 3), (3, 1)]

    for i in range(N):
        if A[i] == B[i]:
            if who_win == 0:
                who_win = 1
            
            else:
                who_win = 0
            
            win = 1
            
        
        elif (A[i], B[i]) in win_case:
            if who_win == 1:
                win += 1
            
            else:
                who_win = 1
                win = 1
        
        else:
            if who_win == 0:
                win += 1
            
            else:
                who_win = 0
                win = 1
        
        result = max(result, win)
    
    print(result)
