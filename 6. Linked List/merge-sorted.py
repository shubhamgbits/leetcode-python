# Definition for singly-linked list.
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


def mergeTwoLists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val > list2.val:
        list1, list2 = list2, list1

    l1 = list1
    l2 = list2
    l1_prev = ListNode(0, l1)

    while l1 is not None and l2 is not None:
        val1 = l1.val
        val2 = l2.val
        if l1.val <= l2.val:
            l1_prev = l1
            l1 = l1.next

        elif l2.val < l1.val:
            l1_prev.next = l2
            next_pointer_l2 = l2.next
            l2.next = l1
            l1 = l2
            l2 = next_pointer_l2

    if l2 is not None:
        l1_prev.next = l2

    return list1

# list1 = [1,2,4], list2 = [1,3,4]

# three1 = ListNode(4, None)
# two1 = ListNode(2, three1)
# one1 = ListNode(1, two1)
#
# three2 = ListNode(4, None)
# two2 = ListNode(3, three2)
# one2 = ListNode(1, two2)

one1 = ListNode(2,None)
one2 = ListNode(1, None)

#mergeTwoLists(one1, one2)
printll(one1)
printll(one2)

printll(mergeTwoLists(one1, one2))

