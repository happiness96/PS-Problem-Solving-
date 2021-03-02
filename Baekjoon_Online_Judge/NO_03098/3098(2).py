# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 03                           | #
# | Day 02                             | #
# | 3098 소셜네트워크                   | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())

    relation = {number: set() for number in range(1, N + 1)}
    
    for _ in range(M):
        A, B =  map(int, r_input().split())
        relation[A].add(B)
        relation[B].add(A)
    
    K = 0
    result = []

    while True:
        new_relation = []

        for my in relation:
            for friend in relation[my]:
                for friend_friend in relation[friend]:
                    if friend_friend == my:
                        continue
                    
                    if friend_friend not in relation[my]:
                        if sorted([my, friend_friend]) not in new_relation:
                            new_relation.append(sorted([my, friend_friend]))
        
        if not new_relation:
            break

        result.append(len(new_relation))

        for A, B in new_relation:
            relation[A].add(B)
            relation[B].add(A)

        K += 1
    
    print(K)
    
    for r in result:
        print(r)


if __name__ == "__main__":
    run()
