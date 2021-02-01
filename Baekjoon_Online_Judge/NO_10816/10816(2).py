# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 01                             | #
# | 10816 숫자 카드 2                   | #
# -------------------------------------- #


def run():
    N = int(r_input())
    cards = sorted(map(int, r_input().split()))

    M = int(r_input())
    numbers = list(map(int, r_input().split()))

    for find in numbers:
        left = 0
        right = 0

        start = 0
        end = N - 1

        while True:
            if end - start <= 1:
                if cards[start] == find:
                    left = start
                
                else:
                    left = end
                
                break
            
            mid = (start + end) // 2

            if cards[mid] >= find:
                end = mid
            
            else:
                start = mid
        
        start = 0
        end = N - 1

        while True:
            if end - start <= 1:
                if cards[end] == find:
                    right = end
                
                else:
                    right = start
                
                break
            
            mid = (start + end) // 2

            if cards[mid] > find:
                end = mid
            
            else:
                start = mid
        
        if cards[left] != find:
            print(0, end=' ')
        
        else:
            print(right - left + 1, end=' ')


if __name__ == "__main__":
    run()
