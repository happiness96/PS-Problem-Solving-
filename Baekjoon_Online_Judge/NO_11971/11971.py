# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 05                             | #
# | 11971 속도 위반                    | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())

    load = []
    car = []
    result = 0

    for _ in range(N):
        length, limit = map(int, r_input().split())

        load.append([length, limit])

    for _ in range(M):
        length, speed = map(int, r_input().split())

        car.append([length, speed])
    
    load = load[::-1]
    car = car[::-1]
    
    while load and car:
        result = max(result, car[-1][1] - load[-1][1])

        if load[-1][0] == car[-1][0]:    
            load.pop()
            car.pop()
        
        elif load[-1][0] > car[-1][0]:
            load[-1][0] -= car[-1][0]
            car.pop()
        
        else:
            car[-1][0] -= load[-1][0]
            load.pop()
    
    print(result)
