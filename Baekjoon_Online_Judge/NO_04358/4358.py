# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 03                           | #
# | Day 02                             | #
# | 4358 생태학                        | #
# -------------------------------------- #


def run():
    save_trees = {}

    total = 0

    for tree in sys.stdin:
        tree = tree.rstrip()

        save_trees[tree] = save_trees.get(tree, 0) + 1
        total += 1
    
    for tree in sorted(save_trees):
        print(tree, '%.4f' % (save_trees[tree] / total * 100))


if __name__ == "__main__":
    run()
