# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 03                           | #
# | Day 02                             | #
# | 10372 Alarm Clock                   | #
# -------------------------------------- #


if __name__ == "__main__":
    n = int(r_input())

    cnt = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    for h in range(24):
        for m in range(60):
            tot = 0
            rep = '%02d%02d' % (h, m)

            for number in rep:
                tot += cnt[int(number)]
            
            if tot == n:
                print(rep[:2] + ':' + rep[2:])
                sys.exit()
    
    print('Impossible')
