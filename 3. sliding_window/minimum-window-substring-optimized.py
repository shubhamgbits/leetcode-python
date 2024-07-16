# key: using dictionary for both string

def solve(s, t):
    t_map, window = {}, {}

    if t == "":
        return ""

    for char in t:
        t_map[char] = 1 + t_map.get(char, 0)

    have, need = 0, len(t_map)

    left = 0
    res, res_length = [-1, -1], float('inf')

    for right in range(len(s)):
        char1 = s[right]

        window[char1] = 1 + window.get(char1, 0)

        if char1 in t_map and window[char1] == t_map[char1]:
            have += 1

        while have == need:
            if (right - left + 1) < res_length:
                res = [left, right]
                res_length = right - left + 1

            window[s[left]] -= 1
            if s[left] in t_map and window[s[left]] < t_map[s[left]]:
                have -= 1

            left += 1

    left, right = res

    return s[left: right + 1] if res_length != float('inf') else ""
