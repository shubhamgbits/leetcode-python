from collections import defaultdict


def solve(strs):
    ans = defaultdict(list) # To handle edge case

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)

    return ans.values()