# -*- encoding: utf-8 -*-
import sys
from heapq import *
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 03                           | #
# | Day 10                             | #
# | 1240 노드사이의 거리                | #
# -------------------------------------- #


def run():
    INF = sys.maxsize
    N, M = map(int, r_input().split())

    distance = [[INF] * (N + 1) for _ in range(N + 1)]
    con = {node: set() for node in range(1, N + 1)}

    for _ in range(N - 1):
        A, B, D = map(int, r_input().split())

        D = min(distance[A][B], D)

        distance[A][B] = D
        distance[B][A] = D
        con[A].add(B)
        con[B].add(A)
    
    for start_node in range(1, N + 1):
        visit = [0] * (N + 1)
        queue = []

        for con_node in con[start_node]:
            queue.append((distance[start_node][con_node], con_node))
        
        visit[start_node] = 1
        heapify(queue)

        while queue:
            dist, node = heappop(queue)
            visit[node] = 1

            for con_node in con[node]:
                if not visit[con_node]:
                    tmp_dist = dist + distance[node][con_node]

                    if tmp_dist < distance[start_node][con_node]:
                        distance[start_node][con_node] = tmp_dist
                        heappush(queue, (tmp_dist, con_node))

    for _ in range(M):
        A, B = map(int, r_input().split())
        print(distance[A][B])


if __name__ == "__main__":
    run()
