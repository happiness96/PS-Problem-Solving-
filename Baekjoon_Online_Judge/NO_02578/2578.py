# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 25                             | #
# | 2578 빙고                          | #
# -------------------------------------- #


def check_bingo():
    bingo = 0

    for i in range(5):
        if chk[i] == [1, 1, 1, 1, 1]:
            bingo += 1
    
    for j in range(5):
        count = 0

        for i in range(5):
            if chk[i][j] == 1:
                count += 1
        
        if count == 5:
            bingo += 1
    
    count = 0
    for i in range(5):
        if chk[i][i] == 1:
            count += 1
    
    if count == 5:
        bingo += 1
    
    count = 0
    for i in range(5):
        if chk[i][4 - i] == 1:
            count += 1
    
    if count == 5:
        bingo += 1
    
    if bingo >= 3:
        return 1
    
    else:
        return 0


if __name__ == "__main__":
    board = [list(map(int, r_input().split())) for _ in range(5)]
    chk = [[0] * 5 for _ in range(5)]
    
    for i in range(5):
        for j, number in enumerate(map(int, r_input().split())):
            flag = 0

            for x in range(5):
                for y in range(5):
                    if board[x][y] == number:
                        chk[x][y] = 1
                        flag = 1
                        break
                
                if flag:
                    break
            
            result = check_bingo()

            if result == 1:
                print(i * 5 + j + 1)
                sys.exit()
