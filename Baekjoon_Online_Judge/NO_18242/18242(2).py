# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 08                             | #
# | 18242 네모네모 시력검사             | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())

    board = []

    left = 0
    right = 0
    flag = 0

    for _ in range(N):
        line = list(r_input().rstrip())
        cnt = line.count('#')

        if not flag:
            if cnt:
                if cnt % 2:
                    left = line.index('#')
                    right = left + cnt
                    flag = 1
                
                else:
                    print('UP')
                    sys.exit()
        
        else:
            if cnt == 1:
                if line[left] == '.':
                    print('LEFT')
                
                else:
                    print('RIGHT')
                
                sys.exit()
            
            elif cnt == 2:
                continue
        
            else:
                print('DOWN')
                sys.exit()
