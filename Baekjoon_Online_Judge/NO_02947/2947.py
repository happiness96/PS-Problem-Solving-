# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 08                             | #
# | 2947 나무 조각                      | #
# -------------------------------------- #


if __name__ == "__main__":
    wood = list(map(int, r_input().split()))
    chk = [1, 2, 3, 4, 5]

    while True:
        if wood[0] > wood[1]:
            wood[0], wood[1] = wood[1], wood[0]

            print(*wood)

            if wood == chk:
                break
        
        if wood[1] > wood[2]:
            wood[1], wood[2] = wood[2], wood[1]

            print(*wood)

            if wood == chk:
                break
                
        if wood[2] > wood[3]:
            wood[2], wood[3] = wood[3], wood[2]

            print(*wood)

            if wood == chk:
                break
                
        if wood[3] > wood[4]:
            wood[3], wood[4] = wood[4], wood[3]

            print(*wood)

            if wood == chk:
                break
        
        if wood == chk:
            print(*wood)
            break
