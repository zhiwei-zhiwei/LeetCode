# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        mid, fast = head, head
        # find the mid point first
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
        midPoint = mid

        left, right = collections.deque(), collections.deque()
        # append the value of the list into deque
        while midPoint:
            left.append(head.val)
            right.appendleft(midPoint.val)
            head = head.next
            midPoint = midPoint.next

        return left == right
