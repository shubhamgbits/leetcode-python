def solve(equation):
    stack = []

    open_brackets = {'{': '}', '[': ']', '(': ')'}

    for bracket in equation:
        if not stack and bracket in open_brackets.values():
            return False

        if bracket in open_brackets:
            stack.append(open_brackets[bracket])

        elif len(stack) != 0 and bracket in open_brackets.values():
            if bracket == stack.pop():
                continue
            else:
                return False

    return True if not stack else False


print(solve("()[{}"))
