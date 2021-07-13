# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 13                             | #
# | 12026 BOJ 거리                      | #
# -------------------------------------- #


def run():
    N = int(r_input())
    words = r_input().rstrip()

    INF = sys.maxsize
    energy = [INF] * N
    energy[0] = 0

    next_dict = {'B': 'O', 'O': 'J', 'J': 'B'}

    for ind in range(N):
        val = energy[ind]

        if val != INF:
            next_word = next_dict[words[ind]]

            for next_ind in range(ind + 1, N):
                if words[next_ind] == next_word:
                    energy[next_ind] = min(energy[next_ind], energy[ind] + (next_ind - ind) ** 2)
    
    if energy[-1] == INF:
        print(-1)
    
    else:
        print(energy[-1])


if __name__ == "__main__":
    run()
