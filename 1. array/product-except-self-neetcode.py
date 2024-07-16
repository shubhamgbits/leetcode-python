def productExceptSelf(nums):
    answer = [1] * len(nums)

    size = len(nums)

    # Initializing final list with prefix values
    for i in range(1, len(nums)):
        answer[i] = answer[i - 1] * nums[i - 1]

    # Very important step of using this postfix variable
    postfix = 1

    for i in range(len(nums) - 2, -1, -1):
        # Updating this postfix value to get desired answer at each step
        postfix *= nums[i + 1]
        answer[i] *= postfix
    return answer


print(productExceptSelf([1,2,3,4]))