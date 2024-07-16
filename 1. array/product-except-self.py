# Time limit exceeded => 18/24 cases passed

def productExceptSelf(nums):
    m = 1

    for num in nums:
        m = m * num

    new_list = []

    for i in range(len(nums)):
        temp_list = nums.copy()
        temp_list.remove(temp_list[i])

        new_list.append(multiplication(temp_list))

    return new_list


def multiplication(nums):
    m = 1

    for num in nums:
        m = m * num

    return m
