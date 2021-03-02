# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 26                             | #
# | 5766 할아버지는 유명해              | #
# -------------------------------------- #


def run():
    while True:
        N, M = map(int, r_input().split())

        if N == M == 0:
            break

        count = {}

        for _ in range(N):
            rank = list(map(int, r_input().split()))

            for number in rank:
                count[number] = count.get(number, 0) + 1
        
        scores = {}

        for key, val in count.items():
            scores[val] = scores.get(val, []) + [key]
        
        print(*sorted(scores[sorted(scores)[-2]]))
    

if __name__ == "__main__":
    run()
