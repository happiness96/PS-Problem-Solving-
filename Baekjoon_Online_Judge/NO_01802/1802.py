# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 07                             | #
# | 1802 종이 접기                      | #
# -------------------------------------- #


def chk_paper(start, end):
    if end - start == 1:
        return True
    
    mid = (start + end) // 2

    left = ''
    right = paper[mid + 1: end]

    for ind in range(mid - 1, start - 1, -1):
        if paper[ind] == '1':
            left += '0'
        
        else:
            left += '1'

    if left != right:
        return False
    
    return chk_paper(start, mid) and chk_paper(mid + 1, end)


if __name__ == "__main__":
    T = int(r_input())

    for _ in range(T):
        paper = r_input().rstrip()

        print('YES' if chk_paper(0, len(paper)) else 'NO')
