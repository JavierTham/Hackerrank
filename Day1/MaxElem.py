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

# Version 2
# We need some way to track the current max number
# might think of storing it in a variable `curr_max`,
# however, problem arises if current max number is popped

# need every number to "remember" max number when they were appended
def getMax(operations):
    stack = []
    memory = [] # to store curr largest number with each append
    arr = []

    for ops in operations:
        query = ops.split(" ")
        op = int(query[0])

        if op == 1:
            num = int(query[1])
            stack.append(num)
    
            # if there's a prev number already
            if memory:
                prev_max = memory[len(memory) - 1]

                # if new number is larger, add it to memory
                if num > prev_max:
                    memory.append(num)

                # else add current largest number again
                else:
                    memory.append(prev_max)

            # if memory is empty
            else:
                memory.append(num)

        elif op == 2:
            stack.pop(len(stack) - 1)
            memory.pop(len(memory) - 1)

        else:
            arr.append(memory[len(memory) - 1])

    return arr

# O(1) time complexity to get current largest number
# O(n) space complexity as we're storing every number in the stack

if __name__ == '__main__':
    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)
    print(res)
