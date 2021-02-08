# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 08                             | #
# | 17488 수강 바구니                   | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())

    limit = [0] + list(map(int, r_input().split()))
    first = [[] for _ in range(M + 1)]
    second = [[] for _ in range(M + 1)]
    success = [[] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for sbj in map(int, r_input().split()):
            if sbj != -1:
                first[sbj].append(i)
    
    for i, st in enumerate(first):
        length = len(st)

        if length <= limit[i]:
            for st_no in st:
                success[st_no].append(i)
            
        limit[i] = max(0, limit[i] - length)
    
    for i in range(1, N + 1):
        for sbj in map(int, r_input().split()):
            if sbj != -1:
                second[sbj].append(i)
    
    for i, st in enumerate(second):
        length = len(st)

        if length <= limit[i]:
            for st_no in st:
                success[st_no].append(i)
    
    for val in success[1:]:
        if val:
            print(*sorted(val))
        
        else:
            print('망했어요')


if __name__ == "__main__":
    run()
