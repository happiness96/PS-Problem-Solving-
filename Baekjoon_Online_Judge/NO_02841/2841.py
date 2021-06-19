# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 19                             | #
# | 2841 외계인의 기타 연주             | #
# -------------------------------------- #


def run():
    N, P = map(int, r_input().split())

    guitar = [[0] for _ in range(7)]
    result = 0

    for _ in range(N):
        line_number, pret = map(int, r_input().split())

        while True:
            if guitar[line_number][-1] > pret:
                guitar[line_number].pop()
                result += 1
            
            else:
                break
        
        if guitar[line_number][-1] != pret:
            guitar[line_number].append(pret)
            result += 1
    
    print(result)


if __name__ == "__main__":
    run()
