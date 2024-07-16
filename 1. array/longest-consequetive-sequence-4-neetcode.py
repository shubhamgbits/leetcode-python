
def solve(nums):
    num_set = set(nums)

    max_len = 0

    for n in nums:
        if n - 1 not in num_set:
            length = 0
            while (n + length) in num_set:
                length += 1
            max_len = max(max_len, length)
    return max_len
