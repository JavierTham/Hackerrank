def isBalanced(s):
    # create empty stack
    stack = []

    # create pairs of brackets with closing ones as key
    bracket_pairs = {")": "(", "]": "[", "}": "{"}

    for bracket in s:

        # current bracket is a closing bracket
        if bracket in bracket_pairs:

            # if stack is empty, it's not valid
            if not stack:
                return "NO"
            
            # get prev bracket
            last_bracket = stack.pop(-1)

            # check if prev bracket is a matching pair
            if not (bracket_pairs[bracket] is last_bracket):
                return "NO"

        # current bracket is an opening bracket
        else:
            stack.append(bracket)

    # all brackets match        
    return "YES"

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        s = input()

        result = isBalanced(s)

        print(result)