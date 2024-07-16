# This solution fails for negative integers 9/76 passed

def solve(nums):
    max_val = 0

    for num in nums:
        if num > max_val:
            max_val = num

    count_map = [0] * (max_val + 1)

    for num in nums:
        count_map[num] += 1

    max_len = 0
    curr_len = 0
    for num in count_map:
        if num > 0:
            curr_len += 1
            max_len = max(max_len, curr_len)
        elif num == 0:
            curr_len = 0

    return max_len
