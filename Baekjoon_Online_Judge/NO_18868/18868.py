# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 03                             | #
# | 18868 멀티버스 Ⅰ                   | #
# -------------------------------------- #


def run():
    M, N = map(int, r_input().split())

    planets = [list(map(int, r_input().split())) for _ in range(M)]

    result = 0

    for A in range(M):
        for B in range(A + 1, M):
            flag = 1

            for i in range(N):
                for j in range(N):
                    if planets[A][i] > planets[A][j] and planets[B][i] > planets[B][j] or planets[A][i] == planets[A][j] and planets[B][i] == planets[B][j] or planets[A][i] < planets[A][j] and planets[B][i] < planets[B][j]:
                        continue
                    flag = 0
                    break
                
                if not flag:
                    break
            
            result += flag
    
    print(result)


if __name__ == "__main__":
    run()
