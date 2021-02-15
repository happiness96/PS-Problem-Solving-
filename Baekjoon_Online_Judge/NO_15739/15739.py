# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 15                             | #
# | 15739 매직스퀘어                   | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    numbers = set()
    board = []
    
    for _ in range(N):
        input_list = list(map(int, r_input().split()))
        board.append(input_list)

        for number in input_list:
            numbers.add(number)

    if len(numbers) != N * N:
        print('FALSE')
        sys.exit()
    
    chk = N * (N ** 2 + 1) // 2

    for row in range(N):
        if sum(board[row]) != chk:
            print('FALSE')
            sys.exit()
    
    for col in range(N):
        total = 0

        for row in range(N):
            total += board[row][col]
        
        if total != chk:
            print('FALSE')
            sys.exit()
    
    total = 0
    for row in range(N):
        total += board[row][row]
    
    if total != chk:
        print('FALSE')
        sys.exit()
    
    total = 0
    for row in range(N):
        total += board[row][N - row - 1]
    
    if total != chk:
        print('FALSE')
        sys.exit()
    
    print('TRUE')
