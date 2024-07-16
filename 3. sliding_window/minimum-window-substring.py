# string 1 = "ADOBECODEBANC",
# string 2 = "ABC"

# if all characters are even available or not

# for minimum window, first and last character of substring should be from string 2

# issue: For next iteration move left pointer or right pointer?? => Backtracking?

# issue: we have to return not just the length but the substring

def solve(str1, str2):
    char_map = {}

    char_map_check = {}

    if len(str1) < len(str2):
        return ""

    for char in str2:
        char_map[char] = 1 + char_map.get(char, 0)

    for char_test in str1:
        char_map_check[char_test] = 1 + char_map_check.get(char_test, 0)

    for key in char_map.keys():
        if key not in char_map_check.keys() or char_map_check[key] < char_map[key]:
            return ""

    right = len(str1) - 1
    left = 0
    for i, char in enumerate(str1[::-1]):
        if char in char_map:
            right = right - i
            break

    for j, char in enumerate(str1):
        if char in char_map:
            left = j
            break

    min_size = len(str1)

    final_right = right
    final_left = left

    while right - left + 1 >= len(str2):

        window = str1[left:right + 1:]

        if not check_substring(window, char_map):
            return ""

        if min_size > right - left + 1:
            final_right = right
            final_left = left
            min_size = len(window) + 1

        right_diff = 0
        left_diff = 0

        for i_right, char_right in enumerate(window[len(window)-2::-1]):
            if char_right in char_map:
                right_diff = i_right
                break

        for i_left, char_left in enumerate(window[1::]):
            if char_left in char_map:
                left_diff = i_left
                break

        if right_diff > left_diff:
            right = right - right_diff - 1
        else:
            left = left + left_diff + 1

    return str1[final_left:final_right + 1]


def check_substring(window, char_map):
    char_map_copy = dict(char_map)

    for char in window:
        if char in char_map_copy.keys():
            char_map_copy[char] -= 1

    if max(char_map_copy.values()) > 0:
        return False
    else:
        return True


answer = solve("acbbaca", "aba")

print("Answer: ", answer)
