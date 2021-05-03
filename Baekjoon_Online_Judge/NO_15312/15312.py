# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 05                           | #
# | Day 03                             | #
# | 15312 이름 궁합                    | #
# -------------------------------------- #


def run():
    alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

    A = r_input().rstrip()
    B = r_input().rstrip()

    save = []

    for ind, val in enumerate(A):
        save.append(alpha[ord(val) - 65])
        save.append(alpha[ord(B[ind]) - 65])
    
    while len(save) != 2:
        new_save = []

        for ind in range(len(save) - 1):
            new_save.append((save[ind] + save[ind + 1]) % 10)
        
        save = new_save
    
    print(*save, sep='')


if __name__ == "__main__":
    run()
