# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 29                             | #
# | 10290 Word Search                  | #
# -------------------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        n, h, w = map(int, r_input().split())

        puzzle = [list(r_input().rstrip()) for _ in range(h)]
        chk = [[0] * w for _ in range(h)]

        flag = 0

        for _ in range(n):
            s = r_input().rstrip()

            if flag == 2:
                continue

            length_s = len(s)

            pi = [0] * length_s

            i = 0
            j = 1

            while j < length_s:
                if s[i] == s[j]:
                    i += 1
                    pi[j] = i
                    j += 1
                
                else:
                    if i == 0:
                        j += 1
                    
                    else:
                        i = pi[i - 1]
            
            find = set()

            steps = []

            for row in range(h):
                steps.append((row, 0, 0, 1))
                steps.append((row, 0, 1, 1))
                steps.append((row, 0, -1, 1))
                steps.append((row, w - 1, 0, -1))
                steps.append((row, w - 1, 1, -1))
                steps.append((row, w - 1, -1, -1))

            for col in range(w):
                steps.append((0, col, 1, 0))
                steps.append((0, col, 1, 1))
                steps.append((0, col , 1, -1))
                steps.append((h - 1, col, -1, 0))
                steps.append((h - 1, col, -1, 1))
                steps.append((h - 1, col, -1, -1))
            
            for row, col, mv_row, mv_col in steps:
                j = 0

                while 0 <= row < h and 0 <= col < w:
                    if puzzle[row][col] == s[j]:
                        row += mv_row
                        col += mv_col
                        j += 1

                        if j == length_s:
                            start = (row - mv_row * length_s, col - mv_col * length_s)
                            end = (row - mv_row, col - mv_col)

                            if start < end:
                                find.add((start, end))
                            
                            else:
                                find.add((end, start))

                            j = pi[j - 2]

                            for cnt in range(1, length_s + 1):
                                chk[row - mv_row * cnt][col - mv_col * cnt] = 1
                    
                    else:
                        if j == 0:
                            row += mv_row
                            col += mv_col
                        
                        else:
                            j = pi[j - 1]

            if not find:
                flag = 2
            
            elif len(find) > 1 and flag < 1:
                flag = 1
        
        if not flag:
            result = ''

            for row in range(h):
                for col in range(w):
                    if not chk[row][col]:
                        result += puzzle[row][col]
            
            if not result:
                print('empty solution')
            
            else:
                print(result)

        elif flag == 1:
            print('ambiguous')
        
        else:
            print('no solution')


if __name__ == "__main__":
    run()
