# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0,head)
        # set a dummy ListNode to store the result

        right = head # this node use to update when find the node need to be skipped
        left = dummy # this node helps to find the end of the ListNode
        for i in range(n):
            # let the right node to run first and set a bundary base on n
            right = right.next
        
        while right:
            # update the pointers one by one, until the right pointer reach the end of the ListNode
            right = right.next
            left = left.next
        
        left.next = left.next.next # replace the node and skip that
        return dummy.next

        # Time complexity : O(len) the length of the listnode
        # Space complexity: O(1)