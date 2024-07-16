def productExceptSelf(nums):
    pre_sum = [1]*len(nums)
    post_sum = [1]*len(nums)

    size = len(nums)

    for i in range(1, len(nums)):
        pre_sum[i] = pre_sum[i-1] * nums[i-1]

    for j in range(len(nums)-2, -1, -1):
        post_sum[j] = post_sum[j+1] * nums[j+1]

    answer = [0]*len(nums)
    for i in range(len(nums)):
        answer[i] = pre_sum[i] * post_sum[i]
    return answer


print(productExceptSelf([1,2,3,4]))