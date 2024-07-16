# Works fine

def solve(nums):
    left = 0
    right = len(nums) - 1

    if nums[left] < nums[right] or len(nums) == 1:
        return nums[left]

    while left < right:
        mid = round((left + right) / 2)

        if left == mid or right == mid:
            return nums[left] if nums[right] > nums[left] else nums[right]

        if nums[mid - 1] > nums[mid] < nums[mid + 1]:
            return nums[mid]

        if nums[mid] <= nums[left]:
            right = mid

        elif nums[mid] > nums[right]:
            left = mid


print(solve([2,3,1]))
