    # -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 05                           | #
# | Day 07                             | #
# | 20546 🐜 기적의 매매법 🐜          | #
# -------------------------------------- #


if __name__ == "__main__":
    J_money = S_money = int(r_input())
    J_stock = S_stock = 0
    stock = list(map(int, r_input().split()))

    inc = 0
    dec = 0

    for ind, stk in enumerate(stock):
        J_stock += J_money // stk
        J_money %= stk

        if ind:
            if stock[ind] - stock[ind - 1] > 0:
                inc += 1
                dec = 0

                if inc >= 3:
                    S_money += stk * S_stock
                    S_stock = 0

            elif stock[ind] - stock[ind - 1] < 0:
                dec += 1
                inc = 0
                
                if dec >= 3:
                    buy = S_money // stk
                    S_stock += buy
                    S_money -= stk * buy
                
            else:
                inc = 0
                dec = 0
        
    J_total = J_money + stock[-1] * J_stock
    S_total = S_money + stock[-1] * S_stock

    print("BNP" if J_total > S_total else "TIMING" if J_total < S_total else "SAMESAME")
