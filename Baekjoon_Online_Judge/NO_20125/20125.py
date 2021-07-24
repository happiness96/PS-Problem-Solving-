# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 24                             | #
# | 20125 쿠키의 신체 측정              | #
# -------------------------------------- #


def run():
    N = int(r_input())

    board = [r_input().rstrip() for _ in range(N)]

    h_x, h_y = 0, 0
    find_head = 0

    for row in range(N):
        for col in range(N):
            if board[row][col] == '*':
                h_x, h_y = row + 1, col
                find_head = 1
                break
        
        if find_head:
            break
    
    left_arm = 0
    right_arm = 0
    waist = 0
    left_leg = 0
    right_leg = 0

    for col in range(h_y - 1, -1, -1):
        if board[h_x][col] == '*':
            left_arm += 1
        
        else:
            break
    
    for col in range(h_y + 1, N):
        if board[h_x][col] == '*':
            right_arm += 1
        
        else:
            break
    
    for row in range(h_x + 1, N):
        if board[row][h_y] == '*':
            waist += 1
        
        if board[row][h_y - 1] == '*':
            left_leg += 1
        
        if board[row][h_y + 1] == '*':
            right_leg += 1
    
    
    print(h_x + 1, h_y + 1)
    print(left_arm, right_arm, waist, left_leg, right_leg)


if __name__ == "__main__":
    run()
