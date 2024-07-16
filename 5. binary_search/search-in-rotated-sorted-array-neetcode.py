def solve(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid

        # Target is in left sorted portion
        if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1

            else:
                right = mid - 1

        # Target in right portion
        else:
            if target > nums[right] or target < nums[mid]:
                right = mid - 1

            else:
                left = mid + 1

    return -1

print(solve([4,5,6,7,8,1,2,3], 8))