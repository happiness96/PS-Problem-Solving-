# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 28                             | #
# | 10431 줄 세우기                     | #
# -------------------------------------- #


def run():
    P = int(r_input())

    for _ in range(P):
        T, *heights = map(int, r_input().split())
        result = 0

        for i in range(20):
            for j in range(i):
                if heights[i] < heights[j]:
                    heights.insert(j, heights.pop(i))
                    result += i - j
                    break
        
        print(T, result)


if __name__ == "__main__":
    run()
