def twoStacks(maxSum, a, b):
    total = 0
    count = 0
    while total < maxSum:
        # if both stacks are not empty
        if a and b:
            # we pick the smaller one
            if a[0] < b[0]:
                # if new sum will be more than maxSum, break
                if total + a[0] > maxSum:
                    break

                # else add to total
                total += a.pop(0)
            else:
                if total + b[0] > maxSum:
                    break

                total += b.pop(0)

            count += 1

        elif a:
            
            total += a.pop(0)
            count += 1
        elif b:
            total += b.pop(0)
            count += 1

        if not (a and b):
            break
    
    return count