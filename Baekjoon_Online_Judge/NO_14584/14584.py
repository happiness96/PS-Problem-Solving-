# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 08                             | #
# | 14584 암호 해독                     | #
# -------------------------------------- #


if __name__ == "__main__":
    password = r_input().rstrip()

    N = int(r_input())
    words = [r_input().rstrip() for _ in range(N)]

    for i in range(26):
        for word in words:
            if word in password:
                print(password)
                sys.exit()
            
        new_password = ''

        for ch in password:
            tmp = ord(ch) + 1

            if tmp > 122:
                tmp = 97
            
            new_password += chr(tmp)
        
        password = new_password
