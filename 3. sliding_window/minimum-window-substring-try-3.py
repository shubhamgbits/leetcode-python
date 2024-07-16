def check_substring(window, char_map):
    window_count = {}
    for char in window:
        window_count[char] = window_count.get(char, 0) + 1

    for char, count in char_map.items():
        if window_count.get(char, 0) < count:
            return False
    return True


def solve(str1, str2):
    char_map = {}
    if str1 == str2:
        return str1
    if len(str2) > len(str1):
        return ""
    for char in str2:
        char_map[char] = char_map.get(char, 0) + 1

    left = 0
    min_len = float('inf')
    min_pos = (0, 0)

    window_count = {}
    for right, char in enumerate(str1):
        if char in char_map:
            window_count[char] = window_count.get(char, 0) + 1

        while check_substring(str1[left:right + 1], char_map):
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_pos = (left, right)
            if str1[left] in char_map:
                window_count[str1[left]] -= 1
            left += 1

    return str1[min_pos[0]:min_pos[1] + 1] if min_len != float('inf') else ""



str1 = "bbaa"
answer = solve(str1, "aba")
print("Answer:", answer)
