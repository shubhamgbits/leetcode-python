# SOLUTION ACCEPTED in ONE GO

# One optimization = To find bread node we can use fast and slow pointer approach

# Even = break node at n / 2
# odd = break node at n / 2 + 1

# Reverse the part after break node
# now just insert the nodes in between of first section from reverse part

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printll(head):
    answer = ""
    while head is not None and head.next is not None:
        answer = answer + str(head.val) + " -> "
        head = head.next

    if head.next is None:
        answer = answer + str(head.val)

    print(answer)


def solve(head):
    head_copy = head

# Finding length
    count = 0
    while head_copy is not None:
        count += 1
        head_copy = head_copy.next
# Calculating breaking point
    breaking_point = count // 2 if count % 2 == 0 else count // 2 + 1

    print("breaking_point = ", breaking_point)
    head_copy = head
    while breaking_point != 0:
        new_head = head_copy.next
        if breaking_point == 1:
            head_copy.next = None

        head_copy = new_head
        breaking_point -= 1

# Reversing later part of LL
    prev = None
    while head_copy is not None:
        prev, head_copy.next, head_copy,  = head_copy, prev, head_copy.next

    reverse_part = prev
    new_head = head

    while reverse_part is not None:
        first_next = new_head.next
        second_next = reverse_part.next

        new_head.next = reverse_part
        reverse_part.next = first_next
        reverse_part = second_next
        new_head = first_next

    return head


# list1 = [1,2,3,4]

one1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
printll(one1)

print(printll(solve(one1)))
