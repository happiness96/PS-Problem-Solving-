# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 06                           | #
# | Day 30                             | #
# | 6613 버그잡는 꿍                    | #
# -------------------------------------- #


def run():
    for inp in sys.stdin:
        T, B = map(str, inp.rstrip().split())

        length_B = len(B)
        pi = [0] * length_B

        i = 0
        j = 1

        while j < length_B:
            if B[i] == B[j]:
                i += 1
                pi[j] = i
                j += 1
            
            else:
                if i == 0:
                    j += 1
                
                else:
                    i = pi[i - 1]

        for _ in range(int(T)):
            code = r_input().rstrip()
            length_code = len(code)

            i = 0
            j = 0

            save = []
            pi2 = [0]

            while i < length_code:
                if code[i] == B[j]:
                    save.append(code[i])
                    i += 1
                    j += 1
                    pi2.append(j)

                    if j == length_B:
                        for _ in range(length_B):
                            save.pop()
                            pi2.pop()
                            
                        j = pi2[-1]

                else:
                    if j == 0:
                        save.append(code[i])
                        i += 1
                        pi2.append(0)
                    
                    else:
                        j = pi[j - 1]
            
            print(''.join(save))


if __name__ == "__main__":
    run()
