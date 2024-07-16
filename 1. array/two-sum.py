# Return indices so cannot use sorting

# Very clever solution to use hashmap and check for target - num

def twoSum(nums, target):
    num_map = {}  # value : index

    for i, num in enumerate(nums):
        if target - num in num_map:
            return [i, num_map[target - num]]

        num_map[num] = i

