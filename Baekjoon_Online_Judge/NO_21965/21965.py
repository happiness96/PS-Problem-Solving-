# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 26                             | #
# | 21965 드높은 남산 위에 우뚝 선       | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    A = [0] + list(map(int, r_input().split()))

    flag = 0

    for ind, val in enumerate(A):
        if not ind:
            continue
        
        if not flag:
            if val == A[ind - 1]:
                print("NO")
                sys.exit()
            
            if val < A[ind - 1]:
                flag = 1
        
        else:
            if val >= A[ind - 1]:
                print("NO")
                sys.exit()
    
    print("YES")