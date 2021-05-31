# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 05                           | #
# | Day 31                             | #
# | 18429 근손실                       | #
# -------------------------------------- #


def use_kit(ind, rem):
    global result

    rem -= K
    rem += A_list[ind]
    visit[ind] = 1

    if rem < 500:
        visit[ind] = 0
        return
    
    if sum(visit) == N:
        result += 1
    
    else:
        for j in range(N):
            if not visit[j]:
                use_kit(j, rem)
    
    visit[ind] = 0


if __name__ == "__main__":
    N, K = map(int, r_input().split())

    A_list = list(map(int, r_input().split()))
    visit = [0] * N

    result = 0

    for i in range(N):
        use_kit(i, 500)
    
    print(result)
