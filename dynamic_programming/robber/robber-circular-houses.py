from typing import List


class Solution:
    def helper(self, nums: List[int]) -> int:
        first = 0
        second = nums[0]

        for i in range(1, len(nums)):
            temp = second
            second = max(second, nums[i] + first)
            first = temp
        return second

    def rob(self, nums: List[int]) -> int:
        if len(nums) in (1, 2, 3):
            return max(nums)

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))


test = [1, 2, 1, 1]

print(Solution().rob(test))
