# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head):
    prev, curr = None, head

    while curr is not None:
        # nxt = curr.next
        # prev = curr
        # curr.next = prev
        # curr = nxt

        curr.next, prev, curr = curr, curr.next, prev

        # (curr.next, prev) = (prev, curr.next)

    return prev

def recursion(head):

    if not head:
        return None

    new_head = head

    if head.next:
        new_head = recursion(head.next)
        head.next.next = head

    head.next = None

    return new_head