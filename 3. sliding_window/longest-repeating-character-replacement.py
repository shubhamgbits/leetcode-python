# Key Step: using dictionary

def characterReplacement(s, k):
    char_hashmap = {}

    max_len = 1
    start_index = 0
    right = 0
    currEnd = 0

    while right < len(s):
        start = s[start_index]
        end = s[right]
        if end not in char_hashmap.keys():
            char_hashmap[end] = 1
        elif currEnd != right:
            char_hashmap[end] += 1

        (max_key, diff) = checkMap(char_hashmap)

        flip_needed = max_key - diff

        if flip_needed == -1 or flip_needed <= k:
            max_len = max(max_len, right-start_index+1)
            right += 1
        else:
            start_index += 1
            char_hashmap[start] -= 1
            currEnd = right

    return max_len


def checkMap(my_dict):

    max_key = max(my_dict, key=my_dict.get)
    flips_needed = my_dict[max_key]

    for key, value in my_dict.items():
        if key != max_key:
            flips_needed -= value

    return my_dict[max_key], flips_needed


length = characterReplacement("AABABBA", 1)

print("Answer = ", length)