from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        first = 0
        second = nums[0]

        for i in range(1, len(nums)):
            temp = second
            second = max(second, nums[i] + first)
            first = temp

        return second


test1 = [1, 2, 3, 1]
test2 = [2, 1, 1, 2]

print(Solution().rob(test2))
