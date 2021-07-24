# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 24                             | #
# | 14646 욱제는 결정장애야!!            | #
# -------------------------------------- #


def run():
    N = int(r_input())

    result = 0
    chk = [0] * (N + 1)
    cur = 0

    for val in map(int, r_input().split()):
        if not chk[val]:
            chk[val] = 1
            cur += 1
            result = max(result, cur)
        
        else:
            cur -= 1
    
    print(result)


if __name__ == "__main__":
    run()
