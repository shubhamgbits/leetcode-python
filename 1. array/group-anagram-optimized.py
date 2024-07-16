from collections import Counter

# Two good things to learn:
# 1) Use of Counter is similar to populating dictionary with character count of words
# 2) use of frozenset to make hashable key


def groupAnagrams(words):
    char_count_map = {}

    for word in words:
        if word == "":
            char_count = "-1"  # Special case for empty string
        else:
            # char_count = frozenset(Counter(word).items())  # Use frozenset for hashable key
            temp_dict = {}
            for char in word:
                temp_dict[char] = 1 + temp_dict.get(char, 0)
            # char_count = frozenset(Counter(word).items())  # Use frozenset for hashable key
            char_count = tuple(temp_dict.items())

        if char_count in char_count_map:
            char_count_map[char_count].append(word)
        else:
            char_count_map[char_count] = [word]

    # Convert the dictionary values to a list
    final_list = list(char_count_map.values())
    return final_list


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))