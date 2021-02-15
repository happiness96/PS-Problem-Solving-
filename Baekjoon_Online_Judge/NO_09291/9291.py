# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 15                             | #
# | 9291 스도쿠 채점                    | #
# -------------------------------------- #


if __name__ == "__main__":
    T = int(r_input())
    chk_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for test_case_no in range(1, T + 1):
        board = [list(map(int, r_input().split())) for _ in range(9)]

        chk1 = 1
        chk2 = 1
        chk3 = 1

        for i in range(9):
            if sorted(board[i]) != chk_list:
                chk1 = 0
        
        for j in range(9):
            save_list = []
            
            for i in range(9):
                save_list.append(board[i][j])
            
            if sorted(save_list) != chk_list:
                chk2 = 0
        
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                save_list = []

                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        save_list.append(board[row][col])
                
                if sorted(save_list) != chk_list:
                    chk3 = 0
        
        print('Case {}: '.format(test_case_no), end='')
        
        if chk1 + chk2 + chk3 != 3:
            print('INCORRECT')
        
        else:
            print('CORRECT')

        r_input()
