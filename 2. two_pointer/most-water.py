# Right pointer initialized incorrectly

def solve(nums):
    left = 0
    right = 1

    max_area = -float('inf')

    while left < right < len(nums) - 1:
        max_area = max(max_area, (right - left) * min(nums[left], nums[right]))

        next_area_1 = (right + 1 - left) * min(nums[left], nums[right + 1])
        next_area_2 = (right + 1 - left - 1) * min(nums[right + 1], nums[left + 1])

        max_area = max(next_area_2, next_area_1)

        if next_area_1 > next_area_2:
            right += 1

        else:
            left += 1

    return max_area


print(solve([1,8,100,2,100,4,8,3,7]))
