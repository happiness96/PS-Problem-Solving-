# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 04                           | #
# | Day 27                             | #
# | 16947 서울 지하철 2호선             | #
# -------------------------------------- #


def run():
    INF = sys.maxsize
    N = int(r_input())

    connected = {node : [] for node in range(1, N + 1)}

    for _ in range(N):
        A, B = map(int, r_input().split())

        connected[A].append(B)
        connected[B].append(A)

    find_cycle = []

    queue = deque([[1, []]])
    cycle_flag = 0

    result = [INF] * (N + 1)
    
    while queue:
        node, visit = queue.popleft()

        for con_node in connected[node]:
            if not visit:
                queue.append([con_node, visit + [node]])
            
            elif con_node != visit[-1]:
                if con_node in visit:
                    cycle_flag = 1
                    
                    for cycle_node in visit[visit.index(con_node):] + [node]:
                        result[cycle_node] = 0
                    
                    break
            
                else:
                    queue.append([con_node, visit + [node]])
        
        if cycle_flag:
            break
    
    new_node = []

    for ind, val in enumerate(result):
        if not val:
            for con_node in connected[ind]:
                if result[con_node]:
                    new_node.append(con_node)

    for node in new_node:
        distance = 1

        queue = deque([node])

        while queue:
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                result[cur_node] = distance

                for con_node in connected[cur_node]:
                    if result[con_node] == INF:
                        queue.append(con_node)
            
            distance += 1
    
    print(*result[1:])


if __name__ == "__main__":
    run()
