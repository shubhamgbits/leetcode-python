# Proud of myself for this solution
# I knew that if this problem needs to be done in O(n), somehow we need to use hashmap smartly
# Time limit exceeded => 72/76 passed

def solve(nums):
    num_map = {}

    for num in nums:
        if num in num_map:
            continue

        elif num + 1 in num_map and num - 1 in num_map:
            num_map[num] = num_map[num + 1] + num_map[num - 1] + 1
            for i in range(1, num_map[num - 1] + 1):
                num_map[num - i] = num_map[num]
            for i in range(1, num_map[num+1] + 1):
                num_map[num+i] = num_map[num]

        elif num - 1 in num_map:
            num_map[num] = num_map[num - 1] + 1
            for i in range(1, num_map[num - 1] + 1):
                num_map[num - i] = num_map[num]

        elif num + 1 in num_map:
            num_map[num] = num_map[num + 1] + 1
            for i in range(1, num_map[num+1] + 1):
                num_map[num+i] = num_map[num]
        else:
            num_map[num] = 1

    return max(num_map.values())


print(solve([1,2,0,1]))