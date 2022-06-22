# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        temp = dummyNode
        outRange = 0
        while l1 or l2:
            l1Val = 0 if l1 is None else l1.val
            l2Val = 0 if l2 is None else l2.val

            sumTemp = l1Val+l2Val+outRange
            store = sumTemp % 10
            outRange = sumTemp // 10
            
            temp.next = ListNode(store)
            temp = temp.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if outRange != 0: temp.next = ListNode(outRange)

        return dummyNode.next
