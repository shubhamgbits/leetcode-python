def solve(nums):
    #target_set = set()

    nums.sort()
    ans = []
    for i, num in enumerate(nums):

        if i > 0 and num == nums[i-1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:

            target = nums[left] + nums[right] + num

            if target > 0:
                right -= 1
            elif target < 0:
                left += 1
            else:
                ans.append([num, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
    return ans


print(solve([0, 0, 0]))
