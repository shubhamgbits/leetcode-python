# Issue: This uses O(n) memory but we can do in O(1) by using original string for comparision

def solve(s: str):
    s = s.lower()

    char_list = []

    for char in s:
        if ord(char) in range(ord('a'), ord('z')+1) or char in range(ord('0'),ord('9')+1):
            char_list.append(char)
    left = 0
    right = len(char_list) - 1

    if len(char_list) == 0 or len(char_list) == 1: return True

    while left <= right:
        if char_list[left] != char_list[right]:
            return False
        left += 1
        right -= 1

    return True


print(solve("0P"))
