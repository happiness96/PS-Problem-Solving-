# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 09                             | #
# | 4913 페르마의 크리스마스 정리      | #
# -------------------------------------- #


def run():
    prime = [1] * 1000001
    can_make = [0] * 1000001

    prime[0] = 0
    prime[1] = 0

    for number in range(4, 1000001, 2):
        prime[number] = 0
    
    for number in range(3, int(1000001 ** 0.5), 2):
        if prime[number]:
            for rem in range(number * 2, 1000001, number):
                prime[rem] = 0
    
    for num1 in range(1, 1001):
        for num2 in range(num1, 1001):
            number = num1 ** 2 + num2 ** 2

            if number < 1000001 and prime[number]:
                can_make[number] = 1
    
    for ind in range(1, 1000001):
        prime[ind] += prime[ind - 1]
        can_make[ind] += can_make[ind - 1]
    
    while True:
        L, U = map(int, r_input().split())

        if L == U == -1:
            break

        print(L, U, prime[max(0, U)] - prime[max(0, L - 1)], can_make[max(0, U)] - can_make[max(0, L - 1)])


if __name__ == "__main__":
    run()
