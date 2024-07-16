start = 5

stack = [start]

print("List Initial: ", stack)

stack.extend([7, 8, 9, 2])

print("List after adding 3 elements: ", stack)

element = stack.pop(0)
print("List after removal: ", stack)
print("List working as QUEUE -> Element removed: ", element)

element = stack.pop()
print("List after removal: ", stack)
print("List working as STACK -> Element removed: ", element)
