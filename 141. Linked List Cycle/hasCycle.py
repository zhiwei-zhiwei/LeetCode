# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # set solution
        # checked = set()
        # while head:
        #     if head in checked:
        #         return True
        #     checked.add(head)
        #     head = head.next
        # return False

        slowPointer, fastPointer = head, head
        # slow moves one step each time
        # fast moves two steps each time

        while fastPointer and fastPointer.next:
            # due to fast need two steps if fast.next.next is null
            # while means fast reach the end of the list, then return False
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

            if slowPointer == fastPointer:
                return True

        return False

        