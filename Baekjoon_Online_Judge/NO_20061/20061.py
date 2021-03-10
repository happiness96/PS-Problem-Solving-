# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 03                           | #
# | Day 10                             | #
# | 20061 모노미노도미노 2              | #
# -------------------------------------- #


def chk_blue(col):
    global score

    flag = 1

    for row in range(4):
        if not blue[row][col]:
            flag = 0
            break
    
    if flag:
        score += 1
        
        for c in range(col, 0, -1):
            for r in range(4):
                blue[r][c] = blue[r][c - 1]
        
        for r in range(4):
            blue[r][0] = 0


def chk_green(row):
    global score

    flag = 1

    for col in range(4):
        if not green[row][col]:
            flag = 0
            break
    
    if flag:
        score += 1

        for r in range(row, 0, -1):
            for c in range(4):
                green[r][c] = green[r - 1][c]
        
        for c in range(4):
            green[0][c] = 0


def chk_zero_one():
    for col in range(2):
        flag = 0

        for row in range(4):
            if blue[row][col]:
                flag = 1
                break
        
        if flag:
            for col in range(5, 0, -1):
                for row in range(4):
                    blue[row][col] = blue[row][col - 1]

            for row in range(4):
                blue[row][0] = 0
    
    for row in range(2):
        flag = 0

        for col in range(4):
            if green[row][col]:
                flag = 1
                break
        
        if flag:
            for row in range(5, 0, -1):
                for col in range(4):
                    green[row][col] = green[row - 1][col]

            for col in range(4):
                green[0][col] = 0


if __name__ == "__main__":
    N = int(r_input())

    blue = [[0] * 6 for _ in range(4)]
    green = [[0] * 4 for _ in range(6)]
    score = 0

    for _ in range(N):
        t, x, y = map(int, r_input().split())

        if t == 1:
            b_col = 0

            for col in range(6):
                if blue[x][col] == 1:
                    break
                b_col = col
            
            blue[x][b_col] = 1

            chk_blue(b_col)

            g_row = 0

            for row in range(6):
                if green[row][y] == 1:
                    break
                g_row = row
            
            green[g_row][y] = 1

            chk_green(g_row)
        
        elif t == 2:
            b_col = 0

            for col in range(6):
                if blue[x][col] == 1:
                    break
                b_col = col
            
            blue[x][b_col - 1] = 1
            blue[x][b_col] = 1

            chk_blue(b_col - 1)
            chk_blue(b_col)

            g_row = 0

            for row in range(6):
                if green[row][y] == 1 or green[row][y + 1] == 1:
                    break
                g_row = row
            
            green[g_row][y] = 1
            green[g_row][y + 1] = 1

            chk_green(g_row)
        
        else:
            b_col = 0

            for col in range(6):
                if blue[x][col] == 1 or blue[x + 1][col] == 1:
                    break
                b_col = col
            
            blue[x][b_col] = 1
            blue[x + 1][b_col] = 1

            chk_blue(b_col)

            g_row = 0

            for row in range(6):
                if green[row][y] == 1:
                    break
                g_row = row
            
            green[g_row - 1][y] = 1
            green[g_row][y] = 1

            chk_green(g_row - 1)
            chk_green(g_row)
        
        chk_zero_one()
    
    cnt = 0

    for r in range(6):
        for c in range(4):
            cnt += blue[c][r] + green[r][c]
    
    print(score)
    print(cnt)
