# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 05                           | #
# | Day 03                             | #
# | 3054 피터팬 프레임                  | #
# -------------------------------------- #


if __name__ == "__main__":
    alpha = r_input().rstrip()

    length = len(alpha)

    for row in range(5):
        if row in (0, 4):
            for cnt in range(1, length + 1):
                if cnt % 3:
                    print('..#.', end='')
                
                else:
                    print('..*.', end='')
            
            print('.')
        
        elif row in (1, 3):
            for cnt in range(1, length + 1):
                if cnt % 3:
                    print('.#.#', end='')
                
                else:
                    print('.*.*', end='')
            
            print('.')
        
        else:
            for cnt in range(1, length + 1):
                if cnt % 3 == 0:
                    print('*.%s.*' % alpha[cnt - 1], end='')
                
                elif cnt == 1 or cnt % 3 == 2:
                    print('#.%s.' % alpha[cnt - 1], end='')
                
                else:
                    print('.%s.' % alpha[cnt - 1], end='')
            
            if length % 3 or length == 1:
                print('#')
            
            else:
                print()

