# -*- encoding: utf-8 -*-
import sys
from collections import deque
from copy import deepcopy
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 07                           | #
# | Day 12                             | #
# | 9079 동전 게임                      | #
# -------------------------------------- #


def run():
    T = int(r_input())
    change = {'H': 'T', 'T': 'H'}

    for _ in range(T):
        coins = [list(map(str, r_input().rstrip().split())) for _ in range(3)]

        visit = set()
        cnt = 0
        
        queue = deque([deepcopy(coins)])
        visit.add(''.join([''.join(coin_row) for coin_row in coins]))

        result_flag = 0

        while queue:
            for _ in range(len(queue)):
                cur_coin = queue.popleft()

                flag = 1
                chk = cur_coin[0][0]

                for row in range(3):
                    for col in range(3):
                        if cur_coin[row][col] != chk:
                            flag = 0
                            break
                    
                    if not flag:
                        break
                
                if flag:
                    print(cnt)
                    result_flag = 1
                    break
        
                for i in range(3):
                    row_coin = deepcopy(cur_coin)
                    col_coin = deepcopy(cur_coin)

                    for j in range(3):
                        row_coin[i][j] = change[row_coin[i][j]]
                        col_coin[j][i] = change[col_coin[j][i]]
                    
                    str_row_coin = ''.join([''.join(coin_row) for coin_row in row_coin])
                    str_col_coin = ''.join([''.join(coin_row) for coin_row in col_coin])
                    
                    if str_row_coin not in visit:
                        visit.add(str_row_coin)
                        queue.append(row_coin)
                    
                    if str_col_coin not in visit:
                        visit.add(str_col_coin)
                        queue.append(col_coin)
                
                dia_coin1 = deepcopy(cur_coin)
                dia_coin2 = deepcopy(cur_coin)

                for i in range(3):
                    dia_coin1[i][i] = change[dia_coin1[i][i]]
                    dia_coin2[i][2 - i] = change[dia_coin2[i][2 - i]]

                    str_dia_coin1 = ''.join([''.join(coin_row) for coin_row in dia_coin1])
                    str_dia_coin2 = ''.join([''.join(coin_row) for coin_row in dia_coin2])

                    if str_dia_coin1 not in visit:
                        visit.add(str_dia_coin1)
                        queue.append(dia_coin1)
                    
                    if str_dia_coin2 not in visit:
                        visit.add(str_dia_coin2)
                        queue.append(dia_coin2)
                        
            if result_flag:
                break        

            cnt += 1
        
        if not result_flag:
            print(-1)


if __name__ == "__main__":
    run()
