# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # checked = set()
        # while head:
        #     if head in checked:
        #         return head
        #     checked.add(head)
        #     head= head.next
        
        # return None

        fastP, slowP = head, head

        firstMeet = False

        while fastP and fastP.next:
            slowP = slowP.next 
            fastP = fastP.next.next
            if slowP == fastP:
                firstMeet = True
                break
        
        if firstMeet:
            temp = head
            while slowP != temp:
                slowP = slowP.next
                temp = temp.next
            return temp 
        else:
            return None