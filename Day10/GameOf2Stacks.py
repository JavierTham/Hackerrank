# maxSum = 10
# 5 1 1 1 1 1
# 1 2 3 4
#
# we can't just pick the smallest element each time


def twoStacks(maxSum, a, b):
    # start off by just picking from 1 stack till maxSum
    max_count = 0
    total = 0

    # use pointer so we reduce time complexity from popping
    a_pointer = 0
    curr_a = a[a_pointer]
    while total + curr_a <= maxSum:
        # add to total, increment count and pointer
        total += curr_a
        max_count += 1
        a_pointer += 1

        if a_pointer >= len(a):
            break

        curr_a = a[a_pointer]
    
    # count now is the max number we can achieve if we only consider stack a
    # we can start taking from the top of stack b to see if it results in a higher count
    # if total < maxSum, we can continue taking -> count increases
    # if total > maxSum, pop off the last added value from stack a and add in the new value from stack b -> count stays the same
    
    b_pointer = 0
    curr_count = max_count

    # iterate through stack b while popping off from stack a if needed
    while b_pointer < len(b) and a_pointer >= 0:
        
        curr_b = b[b_pointer]
        b_pointer += 1

        total += curr_b
        curr_count += 1

        # if new total > maxSum, remove last value from stack a
        while total > maxSum and a_pointer > 0:
            a_pointer -= 1
            total -= a[a_pointer]
            
            curr_count -= 1

        # after adding the value from b and removing from a as needed, check if maximum count increases
        if total <= maxSum and curr_count > max_count:
            max_count = max(max_count, curr_count)

    return max_count

n = int(input())

output = ""

for _ in range(n):
    inp = input().split(" ")
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    max_sum = int(inp[2])

    output += str(twoStacks(max_sum, a, b)) + "\n"

print(output)