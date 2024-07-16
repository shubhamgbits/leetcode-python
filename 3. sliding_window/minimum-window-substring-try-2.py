# Approach :: Backtracking using recursion
# ISSUE: time limit exceeded

def check_substring(window, char_map):
    char_map_copy = dict(char_map)

    for char in window:
        if char in char_map_copy.keys():
            char_map_copy[char] -= 1

    if max(char_map_copy.values()) > 0:
        return False
    else:
        return True


def backtracking(window, left, right, char_map, min_len, min_pos=None):
    # Base Condition

    if left > right or right - left + 1 < sum(char_map.values()):
        return min_len, min_pos

    string_start = window[left]
    string_end = window[right]

    current_window = window[left:right + 1:]

    if not check_substring(current_window, char_map):
        return min_len, min_pos

    # if rightmost or leftmost character does not belong to char_map
    if window[left] not in char_map:
        return backtracking(window, left + 1, right, char_map, min_len)

    elif window[right] not in char_map:
        return backtracking(window, left, right - 1, char_map, min_len)

    new_len = right - left + 1
    if new_len < min_len:
        min_len = new_len
        min_pos = (left, right)

    # Valid case
    return min(backtracking(window, left + 1, right, char_map, right - left + 1, min_pos),
               backtracking(window, left, right - 1, char_map, right - left + 1, min_pos)
               )


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

    window = str1[left:right + 1:]

    answer, pos = backtracking(window, left, right, char_map, 99999999)

    if pos is not None:
        return str1[pos[0]:pos[1] + 1]
    else:
        ""


str1 = "bbaa"

answer = solve(str1, "aba")

print("Answer: ", answer)
