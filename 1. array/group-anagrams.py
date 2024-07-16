# Given an 1. array of strings strs, group the anagrams together. You can return the answer in any order

# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# ---------------------------------------------------------------

# ISSUE: TIME LIMIT EXCEEDED Test cases passed: 111/126
def solve(words):
    final_list = []

    words_copy = words.copy()

    for i, word in enumerate(words_copy):
        if word in words:
            curr_list = [word]
            curr_map = {}
            if word != "":
                for char in word:
                    curr_map[char] = 1 + curr_map.get(char, 0)
            else:
                curr_map["-1"] = 1

            forward_arr = words_copy[i + 1:]

            for j, next_word in enumerate(forward_arr):
                next_word_map = {}

                if next_word == "":
                    next_word_map["-1"] = 1
                else:
                    for next_char in next_word:
                        next_word_map[next_char] = 1 + next_word_map.get(next_char, 0)

                if curr_map == next_word_map:
                    curr_list.append(next_word)
                    while next_word in words:
                        words.remove(next_word)

            final_list.append(curr_list)
    return final_list


print(solve(["", "b", ""]))
