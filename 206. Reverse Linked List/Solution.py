# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre

        '''
        eg:
        pre   curr
        null -> 1 -> 2 -> 3

        temp = 2
        1 -> null
        pre = 1
        curr = 2

        2 -> 1 -> null
        '''
