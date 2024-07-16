# This is my solution BUT
# Completely different approach by neet code

def solve(nums, k):
    num_map = {}

    for num in nums:
        num_map[num] = 1 + num_map.get(num, 0)

    answer = []

    while k > 0:
        max_val = find_max(num_map)
        answer.append(max_val)
        num_map[max_val] = 0
        k -= 1

    return answer


def find_max(my_dict):
    max_value = -1
    max_element = 0
    for key, value in my_dict.items():
        if value > max_value:
            max_value = value
            max_element = key

    return max_element
