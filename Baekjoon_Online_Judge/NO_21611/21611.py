# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 09                             | #
# | 21611 마법사 상어와 블리자드        | #
# -------------------------------------- #


def chk():
    global number

    board_number[number] = (row, col)
    number += 1


def refresh():
    global board

    tmp_list = [0]

    for number, location in board_number.items():
        row, col = location

        if board[row][col]:
            tmp_list.append(board[row][col])
    
    new_board = [[0] * N for _ in range(N)]

    for i in range(min(len(tmp_list), N ** 2)):
        row, col = board_number[i]
        new_board[row][col] = tmp_list[i]
    
    board = new_board


def bomb():
    flag = 0

    num = 0
    locations = []
    cnt = 0

    for _, location in board_number.items():
        row, col = location

        if num == board[row][col]:
            locations.append((row, col))
            cnt += 1
        
        else:
            if cnt >= 4 and num:
                for r, c in locations:
                    board[r][c] = 0
                broken[num] += cnt
                flag = 1

            num = board[row][col]
            locations = [(row, col)]
            cnt = 1
    
    if cnt >= 4 and num:
        for r, c in locations:
            board[r][c] = 0
        broken[num] += cnt
        flag = 1
    
    return flag


def change():
    global board

    tmp_list = [0]

    number = 0
    cnt = 0

    for _, location in board_number.items():
        row, col = location

        if board[row][col] == number:
            cnt += 1
        
        else:
            if number:
                tmp_list.append(cnt)
                tmp_list.append(number)
            
            number = board[row][col]
            cnt = 1
    
    if number:
        tmp_list.append(cnt)
        tmp_list.append(number)
    
    new_board = [[0] * N for _ in range(N)]

    for i in range(min(len(tmp_list), N ** 2)):
        row, col = board_number[i]

        new_board[row][col] = tmp_list[i]
    
    board = new_board



if __name__ == "__main__":
    N, M = map(int, r_input().split())

    board = [list(map(int, r_input().split())) for _ in range(N)]

    broken = [0] * 4

    shark_loc = [N // 2, N // 2]
    mv = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

    board_number = {0: shark_loc}
    row, col = shark_loc
    flag = 0
    number = 1

    for level in range(1, N):
        if not flag:
            for _ in range(level):
                col -= 1
                chk()
            
            for _ in range(level):
                row += 1
                chk()
        
        else:
            for _ in range(level):
                col += 1
                chk()
            
            for _ in range(level):
                row -= 1
                chk()
        
        flag = abs(flag - 1)

    for _ in range(N - 1):
        col -= 1
        board_number[number] = (row, col)
        number += 1

    for _ in range(M):
        d, s = map(int, r_input().split())
        mv_row, mv_col = mv[d]

        for i in range(1, s + 1):
            tmp_row, tmp_col = shark_loc[0] + mv_row * i, shark_loc[1] + mv_col * i
            board[tmp_row][tmp_col] = 0

        refresh()

        while bomb():
            refresh()
        
        change()

    print(broken[1] + broken[2] * 2 + broken[3] * 3)
