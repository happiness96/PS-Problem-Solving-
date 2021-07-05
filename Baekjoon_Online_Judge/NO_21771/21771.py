# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 06                             | #
# | 21771 가희야 거기서 자는 거 아니야   | #
# -------------------------------------- #


if __name__ == "__main__":
    R, C = map(int, r_input().split())

    RG, CG, RP, CP = map(int, r_input().split())

    G_count = 0
    P_count = 0

    for _ in range(R):
        state = r_input().rstrip()
        G_count += state.count('G')
        P_count += state.count('P')
    
    if RG * CG == G_count and RP * CP > P_count:
        print(1)
    
    else:
        print(0)
