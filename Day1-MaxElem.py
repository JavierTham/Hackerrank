import math
import os
import random
import re
import sys

# version 1
# Easiest method that comes to mind is just to initialise an actual stack
# But bad time complexity
def getMax(operations):
    stack = []
    arr = []

    for ops in operations:
        query = ops.split(" ")
        op = int(query[0])
        if op == 1:
            num = int(query[1])
            stack.append(num)
        elif op == 2:
            stack.pop(len(stack) - 1)
        else:
            arr.append(max(stack))
    return arr

if __name__ == '__main__':
    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)
    print(res)