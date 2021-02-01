# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 01                             | #
# | 19949 영재의 시험                   | #
# -------------------------------------- #


def select(choose, cnt, ind, score):
    global result

    score += int(choose == answer[ind])

    if score + (9 - ind) < 5:
        return

    if ind == 9:
        if score >= 5:
            result += 1
        return
    
    for j in range(1, 6):
        if cnt == 2 and j == choose:
            continue
            
        if cnt == 1 and j == choose:
            select(j, cnt + 1, ind + 1, score)
        
        else:
            select(j, 1, ind + 1, score)


if __name__ == "__main__":
    answer = list(map(int, r_input().split()))

    result = 0

    for i in range(1, 6):
        select(i, 1, 0, 0)
    
    print(result)
