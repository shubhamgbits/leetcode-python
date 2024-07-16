def solve(nums):
    num_map = {}

    for num in nums:
        num_map[num] = 1 + num_map.get(num, 0)

    ans = {}

    nums.sort()

    left = 0

    right = len(nums) - 1

    while left < right:

        num1 = nums[left]
        num2 = nums[right]

        target = 0 - num1 - num2

        if (target == num1 and num_map.get(num1, 0) >= 2) \
                or (target == num2 and num_map.get(num2, 0) >= 2) \
                or (num1 != target and num2 != target and target in num_map):

            new_list = tuple(sorted([num1, target, num2]))
            if new_list not in ans:
                ans[new_list] = 1
                left += 1
                right = len(nums) - 1
            else:
                left += 1

        elif right - target < target - left:
            left += 1
        else:
            right -= 1

    return [list(key) for key in ans.keys()]


print(solve([3, 0, -2, -1, 1, 2]))
