# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 03                           | #
# | Day 08                             | #
# | 2805 나무 자르기                    | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())

    heights_dic = {}

    for height in map(int, r_input().split()):
        heights_dic[height] = heights_dic.get(height, 0) + 1

    left = 0
    right = max(heights_dic)

    while True:
        if right - left  <= 1:
            break

        mid = (left + right) // 2
        get = 0

        for height, cnt in heights_dic.items():
            if height > mid:
                get += (height - mid) * cnt
        
        if get < M:
            right = mid
        
        else:
            left = mid

    get = 0

    for height, cnt in heights_dic.items():
        if height > right:
            get += (height - right) * cnt
    
    if get >= M:
        print(right)
    
    else:
        print(left)


if __name__ == "__main__":
    run()
