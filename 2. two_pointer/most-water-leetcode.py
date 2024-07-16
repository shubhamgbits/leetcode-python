def solve(height):
    left = 0
    right = len(height) - 1 # Important to set it to the rightmost to maximize x-axis value

    max_area = -1

    while left < right:
        max_area = max((right - left) * min(height[left], height[right]), max_area)

        if height[left] < height[right]: # Because we want to maximize the area
            left += 1

        else:
            right -= 1

    return max_area


print(solve([1,8,6,2,5,4,8,3,7]))
