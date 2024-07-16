

listExample = [4, 5, 6, 0, 1, 2, 3]
listExample2 = [1, 0]

def findInflection(list):

    if len(list) == 0:
        return 0

    left = 0
    right = 1

    while right < len(list):
        if list[right] < list[left]:
            return right
        left += 1
        right += 1

    if right == len(list) - 1:
        return 0

print(findInflection(listExample2))

