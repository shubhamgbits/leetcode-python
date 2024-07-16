def solve(nums, target):

    left = 0
    right = len(nums) - 1

    if len(nums) == 1 and nums[0] == target:
        return True

    while left < right:

        mid = (left + right) // 2

        if nums[left] < nums[right] or left == mid or right == mid:
            break

        if nums[mid] == target:
            return mid

        if nums[mid] > nums[left] and nums[mid] > target > nums[left]:
            right = mid
            break

        else:
            left = mid

    while left < right:
        mid = (left + right) // 2

        if right - left + 1 == 2:
            if target == nums[left]: return left
            elif target == nums[right]: return right
            else: return -1

        if target == nums[mid]:
            return mid

        if target < nums[mid]:
            right = mid
        else:
            left = mid

    return -1




print(solve([4,5,6,7,8,1,2,3], 8))

