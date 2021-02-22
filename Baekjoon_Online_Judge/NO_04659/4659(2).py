# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 22                             | #
# | 4659 비밀번호 발음하기              | #
# -------------------------------------- #


if __name__ == "__main__":
    while True:
        pw = r_input().rstrip()

        if pw == 'end':
            break

        flag1 = 0
        flag2 = 1
        flag3 = 1

        for vowel in 'aeiou':
            if vowel in pw:
                flag1 = 1
                break
        
        consonant_cnt = 0
        vowel_cnt = 0

        for word in pw:
            if word in 'aeiou':
                if consonant_cnt:
                    consonant_cnt= 0
                    vowel_cnt = 1
                
                else:
                    vowel_cnt += 1

                    if vowel_cnt == 3:
                        flag2 = 0
                        break
                
            else:
                if vowel_cnt:
                    vowel_cnt = 0
                    consonant_cnt = 1
                
                else:
                    consonant_cnt += 1

                    if consonant_cnt == 3:
                        flag2 = 0
                        break
        
        for alphabet in 'abcdfghijklmnpqrstuvwxyz':
            if alphabet * 2 in pw:
                flag3 = 0
                break
        
        print('<' + pw + '> is ', end='')
        
        if flag1 and flag2 and flag3:
            print('acceptable.')
        
        else:
            print('not acceptable.')
