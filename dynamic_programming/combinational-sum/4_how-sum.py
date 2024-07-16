# Similar to canSum problem with one modification => Need to return the pair which forms the target sum
# + return the combination which made the sum possible

def recursion(target_sum, numbers):
    if target_sum == 0:
        return []
    elif target_sum < 0:
        return None

    for number in numbers:
        remainder = target_sum - number
        remainder_result = recursion(remainder, numbers)
        if remainder_result is not None:
            # return remainder_result.append(number) -> does not work
            remainder_result.append(number)
            return remainder_result
    return None


def memoization(target_sum, numbers, mem={}):
    if target_sum in mem:
        return mem[target_sum]
    elif target_sum == 0:
        return []
    elif target_sum < 0:
        return None

    for number in numbers:
        remainder = target_sum - number
        remainder_result = memoization(remainder, numbers, mem)
        if remainder_result is not None:
            # return remainder_result.append(number) -> does not work
            remainder_result.append(number)
            mem[target_sum] = remainder_result
            return mem[target_sum]
    mem[target_sum] = None
    return None


print(recursion(7, [2, 3]))
print(memoization(8, [5, 3, 14]))
