# Numbers can be repeated to get the target sum

# Time Complexity   - O(n^m)
# Space Complexity  - O(m)      => Height of the Tree
def recursion(target_sum, numbers):
    if target_sum < 0:
        return False
    elif target_sum == 0:
        return True

    for number in numbers:
        remainder = target_sum - number
        if recursion(remainder, numbers):
            return True


# Time Complexity   - O(n*m)
# Space Complexity  - O(m)      => Height of the Tree
def memoization(target_sum, numbers, mem={}):
    if target_sum in mem:
        return mem[target_sum]
    elif target_sum < 0:
        return False
    elif target_sum == 0:
        return True

    for number in numbers:
        remainder = target_sum - number
        if memoization(remainder, numbers):
            mem[remainder] = True
            return True

    mem[target_sum] = False
    return False


print(recursion(7, [2, 3]))
# print(recursion(300, [7, 14]))  # Time limit exceed in recursion
print(memoization(7, [2, 3]))
print(memoization(300, [7, 14]))
