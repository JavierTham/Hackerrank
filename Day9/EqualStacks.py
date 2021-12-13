def equalStacks(h1, h2, h3):
    # get sum of all stacks
    s1, s2, s3 = map(sum, [h1, h2, h3])

    # while every stack still have cylinders
    while h1 and h2 and h3:
        # get minimum sum in current iteration
        min_sum = min(s1, s2, s3)
    
        # keep popping off the top till it's less than or equal to the min sum
        while s1 > min_sum:
            s1 -= h1.pop(0)
        while s2 > min_sum:
            s2 -= h2.pop(0)
        while s3 > min_sum:
            s3 -= h3.pop(0)

        # if all 3 are equal, it is the maximum common sum
        if s1 == s2 == s3:
            return s1
    
    # a stack has no more cylinders left
    return 0



if __name__ == "__main__":
    n1, n2, n3 = map(int, input().split(" "))

    h1 = input().split(" ")
    h2 = input().split(" ")
    h3 = input().split(" ")

    equalised_height = equalStacks(h1, h2, h3)

    print(equalised_height)