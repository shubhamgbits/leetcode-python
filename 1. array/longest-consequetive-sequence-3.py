# Same issue as 2nd attempt. But this code looks much cleaner

def solve(nums):
    num_map = {}
    max_length = 0

    for num in nums:
        if num in num_map:
            continue

        left = num_map.get(num-1, 0)
        right = num_map.get(num+1, 0)

        length = left + right + 1

        num_map[num] = length

        for i in range(1, left + 1):
            num_map[num - i] = length
        for i in range(1, right + 1):
            num_map[num + i] = length

        max_length = max(max_length, length)

    return max_length