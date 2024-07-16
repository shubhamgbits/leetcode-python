# Improvements:
# 1) handling first input case in dictionary
# 2) Using for loop. So right always incrementing
# 3) for checking number of flips needed just = window_size - max. occurred alphabet
# 4) only handling >k case

def solve(s, k):
    char_hashmap = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        char_hashmap[s[right]] = 1 + char_hashmap.get(s[right], 0)
        # window = right - left + 1
        if right - left + 1 - max(char_hashmap.values()) > k:
            char_hashmap[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


length = solve("ABAA", 0)

print("Answer = ", length)
