# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 24                             | #
# | 9358 순열 접기 게임                 | #
# -------------------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for tc in range(1, T + 1):
        N = int(r_input())

        numbers = list(map(int, r_input().split()))

        while len(numbers) > 2:
            new_numbers = []

            for i in range(len(numbers) // 2 + len(numbers) % 2):
                new_numbers.append(numbers[i] + numbers[-i - 1])
        
            numbers = new_numbers
        
        print('Case #' + str(tc), end=': ')
        print('Alice' if numbers[0] > numbers[1] else 'Bob')
